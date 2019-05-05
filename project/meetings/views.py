from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting, Participant

# Create your views here.
# 모임 개설
def create(request):
    if request.method == "POST":
        category = request.POST.get('category')
        title = request.POST.get('title')
        writer = request.POST.get('writier')
        min_number = request.POST.get('min_number')
        max_number = request.POST.get('max_number')
        meeting_time = request.POST.get('meeting_time')
        meeting_place = request.POST.get('meeting_place')
        description = request.POST.get('description')
        writer_email = request.POST.get('writer_email')
        password = request.POST.get('password')
        
        meeting = Meeting(category = category, title = title, wrtier = writer, min_number = min_number, max_number = max_number, meeting_time = meeting_time, meeting_place = meeting_place, description = description, writer_email = writer_email, password=password)
        meeting.save()
        return redirect('list')
        
    return render(request, 'meetings/create.html')


# 모임 목록
def list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/list.html', {'meetings':meetings})
    
# 모임 참여 페이지로 넘어가는 것 - id 받아서 다시 넘겨야 함
def join_page(request, id):
    meeting = Meeting.objects.get(pk=id)
    title = meeting.title
    return render(request, 'meetings/join.html', {'title': title})
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

def join(request, id):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        school = request.POST.get('school')
        motive = request.POST.get('motive')
        
        meeting = Meeting(name = name, email = email, school = school, motive = motive)
        meeting.save()
        return redirect('meetings:list')
        

# 모임 수정 페이지 띄우기
def edit(request, id):
        meeting = get_object_or_404(Meeting, pk=id)
        return render(request, 'meetings/edit.html', {'meeting':meeting})


# 모임 수정
def update(request, id):
    if request.method == "POST":
        meeting = get_object_or_404(Meeting, pk=id)
        category = request.POST.get('category')
        title = request.POST.get('title')
        writer = request.POST.get('writier')
        min_number = request.POST.get('min_number')
        max_number = request.POST.get('max_number')
        meeting_time = request.POST.get('meeting_time')
        meeting_place = request.POST.get('meeting_place')
        description = request.POST.get('description')
        writer_email = request.POST.get('writer_email')

        meeting.category = category
        meeting.title = title
        meeting.writer = writer
        meeting.min_number = min_number
        meeting.max_number = max_number
        meeting.meeting_time = meeting_time
        meeting.meeting_place = meeting_place
        meeting.description = description
        meeting.writer_email = writer_email

        meeting.save()

        return redirect('meetings:read', meeting.pk)

# 모임 삭제하기
def delete(request, id):
    if request.method == "POST":
        meeting = Meeting.objects.get(pk=id)
        meeting.delete()
        return redirect('meeting:list')
        
        
# 모임 상세보기
def read(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    default_view_count = meeting.view_count
    meeting.view_count = default_view_count + 1
    meeting.save()
    return render(request, 'meeting/read.html', {'meeting': meeting})


def verification(request):
    return render(request, 'meetings/verification.html')