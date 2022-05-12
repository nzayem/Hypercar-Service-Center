from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from collections import deque


ticket_number = 0
next_ticket = 0
oil_queue = deque()
tires_queue = deque()
diagnostic_queue = deque()

lines_of_cars = {
    'oil': oil_queue,
    'tires': tires_queue,
    'diagnostic': diagnostic_queue
}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class ChangeOilView(View):

    def get(self, request, *args, **kwargs):

        global ticket_number

        ticket_number += 1
        timer = 2 * len(oil_queue)
        oil_queue.appendleft(ticket_number)
        print('Oil:', len(oil_queue), len(tires_queue), len(diagnostic_queue))
        print('Oil_timer:', timer)

        return render(request, 'oil.html', {'timer': timer, 'number': ticket_number})


class InflateTiresView(View):

    def get(self, request, *args, **kwargs):
        global ticket_number

        ticket_number += 1
        timer = 2 * len(oil_queue) + 5 * len(tires_queue)
        tires_queue.appendleft(ticket_number)
        print('Tires:', len(oil_queue), len(tires_queue), len(diagnostic_queue))

        return render(request, 'tires.html', {'timer': timer, 'number': ticket_number})


class DiagnosticView(View):

    def get(self, request, *args, **kwargs):
        global ticket_number

        ticket_number += 1
        timer = 2 * len(oil_queue) + 5 * len(tires_queue) + 30 * len(diagnostic_queue)
        diagnostic_queue.appendleft(ticket_number)
        print('Diag:', len(oil_queue), len(tires_queue), len(diagnostic_queue))

        return render(request, 'diagnostic.html', {'timer': timer, 'number': ticket_number})


class OperatorView(View):

    def post(self, request, *args, **kwargs):

        global next_ticket

        if len(oil_queue):
            next_ticket = oil_queue.pop()
        elif len(tires_queue):
            next_ticket = tires_queue.pop()
        elif len(diagnostic_queue):
            next_ticket = diagnostic_queue.pop()

        print(len(oil_queue), len(tires_queue), len(diagnostic_queue))
        print('next ticket in operator view:', next_ticket)

        return redirect(reverse('next'))

    def get(self, request, *args, **kwargs):

        context = {
            'oil_queue': len(oil_queue),
            'tires_queue': len(tires_queue),
            'diagnostic_queue': len(diagnostic_queue)
        }

        return render(request, 'operator.html', context)


class NextTicketView(View):

    def get(self, request, *args, **kwargs):

        global next_ticket
        print('ticket in next View:', next_ticket)
        return render(request, 'next.html', {'ticket': next_ticket})
