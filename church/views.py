from django.conf import settings
from django.shortcuts import render, redirect
from .models import Event, Comment, signUp, Grouped, chosenGroup, Service, Staff, Video, Audio, Document, Image, \
    attendanceList, Pledge,Responses
from django.views.generic.edit import UpdateView, CreateView, View
from try1.forms import Userform, Queries, Response, SignForm, Attend, Contribution, JoinGroup
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
import time
from django.core.mail import send_mail



# Create your views here.
def docket1(request):
    events = Event.objects.order_by('date')
    query = Comment.objects.all()
    return render(request, 'church/timetable.html',
                  {'events': events, 'queries': query})


@login_required
def docket2(request, username):
    events = Event.objects.order_by('date')
    query = Comment.objects.all()
    user = signUp.objects.get(user__username=username)
    person = signUp.objects.all()
    return render(request, 'itinerary/timetable.html',
                  {'events': events, 'queries': query, 'people': person, 'user': user, 'username': username})


class Update(UpdateView):
    model = Event
    fields = ['event', 'description', 'date', 'person_in_charge', 'venue']


class Action(CreateView):
    model = Event
    fields = ['event', 'description', 'date', 'person_in_charge', 'venue']


@login_required
def topic_detail(request, topic):
    subject = Event.objects.get(pk=topic)
    return render(request, 'itinerary/topic.html', {'topic': subject})


@login_required
def tutor_detail_staff(request, tutor):
    person = signUp.objects.get(full_name=tutor)
    return render(request, 'itinerary/tutor.html', {'person': person})


@login_required
def tutor_detail_member(request, username, tutor):
    person = signUp.objects.get(full_name=tutor)
    user = signUp.objects.get(user__username=username)
    return render(request, 'church/tutor.html', {'person': person, 'username': username, 'user': user})


@login_required
def member_detail(request, username, group, tutor):
    person = signUp.objects.get(full_name=tutor)
    group = Grouped.objects.get(group=group)
    user = signUp.objects.get(user__username=username)
    groops = Grouped.objects.all()
    return render(request, 'itinerary/member.html',
                  {'person': person, 'group': group, 'groups': groops, 'username': username, 'user': user})


@login_required
def profile(request, username):
    person = signUp.objects.get(user__username=username)
    user = signUp.objects.get(user__username=username)
    return render(request, 'church/profile.html',
                  {'person': person, 'username': username, 'user': user})


@login_required
def detailgroup(request, username, group):
    members = signUp.objects.all()
    user = signUp.objects.get(user__username=username)
    grup = Grouped.objects.get(group=group)
    present = 0
    for tool in grup.tool_set.all():
        if tool:
            present += 1
    for member in members:
        for gryp in member.chosengroup_set.all():
            if gryp.group == group:
                for person in grup.member_set.all():
                    if person.member == member.full_name:
                        gryp.delete()
    return render(request, 'itinerary/groupdetail.html',
                  {'groups': grup, 'members': members, 'present': present, 'username': username, 'user': user})


@login_required
def grouptool(request, username, group):
    tool = Grouped.objects.get(group=group)
    user = signUp.objects.get(user__username=username)
    return render(request, 'itinerary/tool.html', {'groups': tool, 'user': user, 'username': username})


class Creategroup(LoginRequiredMixin, View):
    form_class = JoinGroup

    def get(self, request, username, group):
        form = self.form_class()
        return render(request, 'church/chosengroup_form.html', {'form': form, 'username': username, 'group': group})

    def post(self, request, username, group):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('church:detailgroup', **{'group': group, 'username': username})

        return render(request, 'church/chosengroup_form.html', {'username': username, 'group': group})


@login_required
def exit(request, username, user, group):
    leaver = chosenGroup.objects.get(user=user, group=group)
    leaver.delete()
    return redirect('church:detailgroup', **{'username': username, 'group': group})


@login_required
def groups(request, username):
    group = Grouped.objects.all()
    user = signUp.objects.get(user__username=username)
    return render(request, 'grouplist.html', {'groups': group, 'username': username, 'user': user})





@login_required
def member(request, username):
    staff = Staff.objects.all()
    user = signUp.objects.get(user__username=username)
    return render(request, 'itinerary/members.html', {'staff': staff, 'user': user, 'username': username})


def member2(request):
    staff = Staff.objects.all()
    return render(request, 'itinerary/members2.html', {'staff': staff})


class Addgroup(LoginRequiredMixin,View):
    form_class = Group
    template_name = 'itinerary/addgroup.html'

    def get(self, request, person):
        form = self.form_class()
        return render(request, self.template_name, {'myform': form})

    def post(self, request, person):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            return redirect('church:groups')

        return render(request, self.template_name, {'myform': form})


@login_required
def service(request, username):
    services = Service.objects.all()
    users = signUp.objects.get(user__username=username)
    return render(request, 'itinerary/services.html', {'services': services, 'user': users, 'username': username})


@login_required
def servicedetail(request, service, username):
    user = signUp.objects.get(user__username=username)
    offer = Service.objects.get(service=service)
    return render(request, 'itinerary/servicedetail.html', {'service': offer, 'user': user, 'username': username})


@login_required
def videos(request, username):
    video = Video.objects.all()
    user = signUp.objects.get(user__username=username)
    return render(request, 'itinerary/videos.html', {'videos': video, 'user': user, 'username': username})


@login_required
def audios(request, username):
    audio = Audio.objects.all()
    user = signUp.objects.get(user__username=username)
    return render(request, 'itinerary/audios.html', {'audios': audio, 'user': user, 'username': username})


@login_required
def documents(request, username):
    document = Document.objects.all()
    user = signUp.objects.get(user__username=username)
    return render(request, 'itinerary/documents.html', {'documents': document, 'user': user, 'username': username})


@login_required
def images(request, username):
    group = Grouped.objects.all()
    user = signUp.objects.get(user__username=username)
    return render(request, 'itinerary/images.html', {'group': group, 'user': user, 'username': username})


class Sign_up(View):
    user_form_class = Userform
    profile_form_class = SignForm
    template_name = 'signup.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = self.user_form_class(data=request.POST)
        profile_form = self.profile_form_class(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            #send_mail(subject, message, from_mail, reciepients,fail_silently = True)
            subject = "Thanks for signing up"
            message = f"Welcome {username},\n\nYou have successfully signed up for OMSOM. Get ready to view various features on our website.\n\nEnjoy"
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email, settings.EMAIL_HOST_USER,]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('base', **{'username': username})


        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class UpdateProfile(LoginRequiredMixin,UpdateView):
    model = signUp
    fields = ['gender', 'nationality', 'address', 'relationship_status', 'profile', 'tel_number',
              'occupation', 'profile_picture']



class Pledges(LoginRequiredMixin,View):
    form_class = Contribution
    template_class = 'church/pledges.html'

    def get(self, request, username, group):
        form = self.form_class()
        return render(request, self.template_class, {'form': form, 'group': group, 'username': username})

    def post(self, request, username, group):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('church:detailgroup', **{'username': username, 'group': group})
        return render(request, self.template_class, {'form': form, 'group': group, 'username': username})


@login_required
def expel(request, username, group, user):
    criminal = Pledge.objects.get(person=user)
    criminal.delete()
    return redirect('church:detailgroup', **{'username': username, 'group': group})


class Attendance(LoginRequiredMixin, View):
    form_class = Attend
    template_name = 'itinerary/attendance.html'

    def get(self, request, username, event):
        form = self.form_class()
        return render(request, self.template_name, {'myform': form, 'username': username})

    def post(self, request, username, event):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            return redirect('church:eventmember', **{'username': username})

        return render(request, self.template_name, {'myform': form, 'username': username})


class Question(LoginRequiredMixin, View):
    form_class = Queries
    template_name = 'itinerary/query.html'

    def get(self, request, username):
        form = self.form_class(None)
        return render(request, self.template_name, {'yform': form, 'username': username})

    def post(self, request, username):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            return redirect('church:eventmember', **{'username': username})

        return render(request, self.template_name, {'yform': form, 'username': username})


class Respond(LoginRequiredMixin, View):
    form_class = Response
    template_name = 'itinerary/response.html'

    def get(self, request, username):
        form = self.form_class()
        return render(request, self.template_name, {'myform': form, 'username': username})

    def post(self, request, username):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            return redirect('church:eventmember', **{'username': username})

        return render(request, self.template_name, {'myform': form, 'username': username})

@login_required
def deleteresponse(request,username,name,answer):
    item = Responses.objects.get(answer=answer,full_name=name)
    item.delete()
    return redirect('church:eventmember',**{'username': username})


@login_required
def deletequery(request, username,name, pk):
    item = Comment.objects.get(pk=pk,person=name)
    item.delete()
    return redirect('church:eventmember', **{'username': username})
