from django.shortcuts import render


# Create your views here.

# 添加 index 函数，返回 index.html 页面
def index(request):
    return render(request, 'index.html')


# 添加 search 函数，返回 search.html 页面
def search(request):
    return render(request, 'search.html')


# 执行查询操作
def doSearch(request):
    samplecode = request.GET.get("sampleCode")
    print("需要检验的样本编号是：" + samplecode)
    if samplecode == '1':
        return render(request, 'search.html', {'result': '是芯片'})
    if samplecode == '2':
        return render(request, 'search.html', {'result': '是panel'})
    else:
        return render(request, 'search.html', {'result': '无此样本编号'})
