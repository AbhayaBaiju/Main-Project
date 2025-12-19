from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        a=request.POST.get("txt_num1")
        b=request.POST.get("txt_num2")
        c=int(a)+int(b)
        return render(request,'Basics/Sum.html',{'Sum':c})
    else:
        return render(request,'Basics/Sum.html')
def Calculator(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        btn=request.POST.get("btn_submit")
        if btn=="+":
            c=a+b
        elif btn=="-":
            c=a-b
        elif btn=="*":
            c=a*b
        elif btn=="/":
            c=a/b
        return render(request,'Basics/Calculator.html',{'Calc':c})
    else:
        return render(request,'Basics/Calculator.html')
def Largest(request):
    if request.method=="POST":
        a=int(request.POST.get("txt_num1"))
        b=int(request.POST.get("txt_num2"))
        c=int(request.POST.get("txt_num3"))
        btn=0
        if a>b and a>c:
            btn=a
        elif b>a and b>c:
            btn=b
        elif c>a and c>b:
            btn=c
        return render(request,'Basics/Largest.html',{'Lar':btn})
    else:
        return render(request,'Basics/Largest.html')