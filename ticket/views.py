import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Ticket
from .form import CreateTicketForm, UpdateTicketForm

"""For Coustomers"""

# creating a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = 'Pending'
            var.save()
            messages.info(request, 'Your ticket has been successfully submitted. An engineer would be assigned soon')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context - {'form':form}
        return render(request, 'ticket/create_ticket.html', context)
    

#updating a ticket
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save
            messages.info(request, 'Your ticket info has been updated and all the changes are saved in the database')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            # return redirect('create-ticket')
    else:
        form = UpdateTicketForm(instance=ticket)
        context - {'form':form}
        return render(request, 'ticket/update_ticket.html', context)
