from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Profile, Associate
from .forms import SignUpForm, AssociateForm
from .serializer import ProfileSerializer

MODEL_BACKEND = settings.MODEL_BACKEND

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  context = {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }
  print(context)

  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


def signup_view(request, *args, **kwargs):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user, backend=MODEL_BACKEND)
      return redirect('profile_api')
  else:
    form = SignUpForm()
  return render(request, "user/signup.html", {'form': form})

@api_view(['GET', 'POST'])
def login_api(request, *args, **kwargs):
  print(request.data)
  return Response(request.data)

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def auth_api(request, *args, **kwargs):
  token = Token.objects.get(user=request.user)
  content = {
      'user': str(request.user),  # `django.contrib.auth.User` instance.
      'auth': str(request.auth),  # None
      'token': str(token),  # None
  }
  print(content)
  return Response(content)

 
@api_view(['GET'])
def profiles_api(request, *args, **kwargs):
  if request.user.is_authenticated:
    print(request.user)
  queryset = get_list_or_404(Profile)
  serialized_profile = ProfileSerializer(queryset, many=True)

  return Response(serialized_profile.data)

@api_view(['GET'])
def profile_detail_api(request, id, *args, **kwargs):
  if request.user.is_authenticated:
    print(request.user)
  query = get_object_or_404(Profile, pk=id)
  serialized_profile = ProfileSerializer(query)

  return Response(serialized_profile.data)


@api_view(['GET', 'POST'])
def invite_user_api(request, id, *args, **kwargs):
  print(request.user)
  if request.method == 'POST':
    print(request.data)
  return Response(request.data)



def profile_view(request,*args, **kwargs):
  post = request.POST
  user = request.user
  if user.is_authenticated:
    context = {
      'profile': user,
      'invites_sent': None,
      'invites_received': None,
    }
    if request.method=='GET': 
      context['invites_sent'] = Associate.objects.filter(sender=request.user)
      context['invites_received'] = Associate.objects.filter(receiver=request.user)
      context['form'] = AssociateForm() 
      invites_sent = Associate.get_sent_invites(Associate, request.user)
      invites_received = Associate.get_received_invites(Associate, request.user)
      # invites_status = Associate.get_invite_status(Associate, )
      
      context['peer_invites']  = {
        "sent": invites_sent,
        "received": invites_received,
        # "sent": invites_sent,
        }
      print(context['peer_invites'] )
    elif request.method=='POST':
      form = AssociateForm(request.POST)
      print(form)
      # status = post['status']
      # instance = form.save(commit=False)
      # instance.status = status
      # form.save() 
      context['form'] = form
  return render(request, "user/profile.html", context)


def profile_list_view(request, slug, *args, **kwargs):
  if request.method == 'GET':
    pass
  return render(request, "user/profile-list.html", {'profile_list': 'hello fucker!'})
