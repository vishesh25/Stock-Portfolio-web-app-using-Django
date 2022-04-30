from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, report, mail_report
from django.http import HttpResponseRedirect
from .forms import PortfolioForm
from .forms import UpdatePortfolioForm
from .utils import get_total_purchased_price, get_total_current_price, get_plot_bar
# Create your views here.


@login_required
def HomeView(request):
    purchased_amount = get_total_purchased_price(request)
    current_value = get_total_current_price(request)
    net_gain_loss = float(current_value) - float(purchased_amount)
    bar = get_plot_bar(purchased_amount, current_value)
    if purchased_amount == 0.00:
        return render(request, 'portfolio/home.html', {})
    return render(request, 'portfolio/home.html', {'purchase': "₹{0:0,.2f}".format(purchased_amount),
                                                   'current': "₹{0:0,.2f}".format(current_value),
                                                   'net': "{0:0,.2f}".format(net_gain_loss),
                                                   'bar': bar})


class CreateInterfaceView(LoginRequiredMixin, CreateView):
    model = models.Stocks
    success_url = '/portfolio/my_details'
    login_url = '/home/login'
    form_class = PortfolioForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateInterfaceView(LoginRequiredMixin, UpdateView):
    model = models.Stocks
    success_url = '/portfolio/my_details'
    login_url = '/home/login'
    form_class = UpdatePortfolioForm

    def get_queryset(self):
        return self.request.user.portfolio.all()


class DeleteInterfaceView(LoginRequiredMixin, DeleteView):
    model = models.Stocks
    success_url = '/portfolio/my_details'
    login_url = '/home/login'
    template_name = 'portfolio/stock_delete.html'


class StockListView(LoginRequiredMixin, ListView):
    model = models.Stocks
    context_object_name = 'portfolio'
    template_name = 'portfolio/my_details.html'
    login_url = '/home/login'

    def get_queryset(self):
        return self.request.user.portfolio.all()


def SendMail(request):
    if report.generate_csv(request):
        if mail_report.mail_report("{0} {1}".format(request.user.first_name, request.user.last_name),
                                   request.user.email):
            return render(request, "mail/mail_success.html", {})
        else:
            return render(request, "mail/mail_failure.html", {})
    else:
        return render(request, "mail/report_failure.html", {})
