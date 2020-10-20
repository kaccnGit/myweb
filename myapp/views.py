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
    print(request)
    print("需要检验的样本编号是：" + samplecode)
    if samplecode == '1':
        return render(request, 'search.html', {'samplecode':samplecode,'result': '能够生成'})
    if samplecode == '2':
        return render(request, 'search.html', {'samplecode':samplecode,'result': '是panel'})
    else:
        return render(request, 'search.html', {'samplecode':samplecode,'result': '无此样本编号'})

# 添加 execute 函数，返回 execute.html 页面
def execute(request):
    return render(request, 'execute.html')


# 执行查询操作
def doExecute(request):
    samplecode = request.GET.get("sampleCode")
    print("需要上传检测结果的样本编号是：" + samplecode)
    #开始上传

    #上传结束

    if samplecode == '1':
        return render(request, 'execute.html', {'samplecode':samplecode,'result': '上传结果生成报告执行成功！'})
    else:
        return render(request, 'execute.html', {'samplecode':samplecode,'result': '执行失败！'})