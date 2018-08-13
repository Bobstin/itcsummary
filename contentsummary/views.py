from django.shortcuts import render

import pdb

from .models import Session, Quote, KeyTakeaway, Speech


# Create your views here.
def example(request):
    session = Session.objects.all().order_by('number')[0]
    session = sessioninfo(session)
    context = {'session': session}

    return render(request, 'contentsummary/example.html', context)


def nextSession(request, priornumber):
    nextnumber = int(priornumber) + 1
    session = Session.objects.get(number=nextnumber)
    session = sessioninfo(session)
    context = {'session': session}

    return render(request, 'contentsummary/session.html', context)


def singleSession(request, session_number):
    # pdb.set_trace()
    session = Session.objects.get(number=session_number)

    sessions = [{'session': session,
                 'quotes': Quote.objects.filter(session=session),
                 'keytakeaways': KeyTakeaway.objects.filter(session=session),
                 'speakers': Speech.objects.filter(session=session),
                 }]

    context = {'sessions': sessions}

    return render(request, 'contentsummary/all_sessions.html',context)


def allSessions(request):
    db_sessions = Session.objects.all()

    sessions = [
    {
    'session':session,
    'quotes':Quote.objects.filter(session=session),
    'keytakeaways':KeyTakeaway.objects.filter(session=session),
    'speakers':Speech.objects.filter(session=session),
    } for session in db_sessions
    ]

    context = {'sessions':sessions}

    return render(request,'contentsummary/all_sessions_no_resize.html',context)


def allSessionspt1(request):
    db_sessions = Session.objects.filter(number__lte=26)

    sessions = [
    {
    'session':session,
    'quotes':Quote.objects.filter(session=session),
    'keytakeaways':KeyTakeaway.objects.filter(session=session),
    'speakers':Speech.objects.filter(session=session),
    } for session in db_sessions
    ]

    db_sessions = Session.objects.filter(number__gte=27)
    sessions += [
    {
    'session':session,
    'quotes':Quote.objects.filter(session=session),
    'keytakeaways':KeyTakeaway.objects.filter(session=session),
    'speakers':Speech.objects.filter(session=session),
    } for session in db_sessions
    ]

    context = {'sessions':sessions}

    return render(request,'contentsummary/all_sessions_no_resize.html',context)


def allSessionspt2(request):
    db_sessions = Session.objects.filter(number__gte=27)

    sessions = [
    {
    'session':session,
    'quotes':Quote.objects.filter(session=session),
    'keytakeaways':KeyTakeaway.objects.filter(session=session),
    'speakers':Speech.objects.filter(session=session),
    } for session in db_sessions
    ]

    db_sessions = Session.objects.filter(number__lte=26)
    sessions += [
    {
    'session':session,
    'quotes':Quote.objects.filter(session=session),
    'keytakeaways':KeyTakeaway.objects.filter(session=session),
    'speakers':Speech.objects.filter(session=session),
    } for session in db_sessions
    ]

    context = {'sessions': sessions}

    return render(request, 'contentsummary/all_sessions_no_resize.html', context)


def sessioninfo(session):
    sessioninfo = {'session': session,
                   'quotes': Quote.objects.filter(session=session),
                   'keytakeaways': KeyTakeaway.objects.filter(session=session),
                   'speakers': Speech.objects.filter(session=session), }
    return sessioninfo