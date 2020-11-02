from django.shortcuts import render
import csv
import json
import requests


# Create your views here.

# 添加 index 函数，返回 index.html 页面
def index(request):
    return render(request, 'index.html')


# 添加 search 函数，返回 search.html 页面
def search(request):
    return render(request, 'search.html')


def load_json(json_file):
    try:
        with open(json_file, 'r') as fileio:
            string = fileio.read()
            json_data = json.loads(string)
    except IOError:
        print("Error: cannot open {}!".format(json_file))
        json_data = ''
    return json_data

def get_config_info(config):
    config_data = load_json(config)
    type_file = config_data['sample_type_file']
    try:
        with open(type_file, 'r') as fileio:
            reader = csv.DictReader(fileio, delimiter='\t')
            type_info = {row['sample']: row['type'] for row in reader}
    except IOError:
        print("Error: cannot open {}!".format(type_file))

    upload_args = config_data['upload_args']
    return type_info, upload_args

def upload_report(samplecode, upload_args):

    sample_report = load_json('%s/%s.upload_report.json' % (upload_args['report_path'], samplecode))
    if sample_report:
        data = json.loads(json.dumps(sample_report))
        retry = 0
        while retry < 5:
            retry += 1
            try:
                response = requests.post(upload_args['url'], json=data, headers=upload_args['headers'])
            except Exception:
                print('Error in url POST method')
            if response.ok:
                msg = json.loads(response.texxt)
                infoCode = str(msg.get('infoCode', 'no infoCode'))
                text = response.text.encode('utf-8')
                if infoCode == '2000':
                    result = u'上传成功'
                    break
                elif infoCode == '2100':
                    result = u'样本不存在,上传失败'
                    break
                elif infoCode == '3500':
                    result = u'不能重复上传,上传失败'
                    break
                else:
                    result = u'上传失败'
        else:
            result = u'上传失败'
    else:
        result = u'未找到报告,上传失败'
    return result


# 执行查询操作
def doSearch(request):
    samplecode = request.GET.get("sampleCode")
    config = request.GET.get("config")
    print(request)
    print("需要检验的样本编号是：" + samplecode)
    #读取配置文件
    type_info, upload_args = get_config_info(config)
    sample_type = type_info.get(samplecode, 'NA')

    if sample_type == 'array':
        return render(request, 'search.html', {'samplecode':samplecode,'result': '芯片样本'})
    if sample_type == 'panel':
        return render(request, 'search.html', {'samplecode':samplecode,'result': 'panel样本'})
    else:
        return render(request, 'search.html', {'samplecode':samplecode,'result': '无此样本编号'})

# 添加 execute 函数，返回 execute.html 页面
def execute(request):
    return render(request, 'execute.html')


# 执行查询操作
def doExecute(request):
    samplecode = request.GET.get("sampleCode")
    config = request.GET.get("config")
    print("需要上传检测结果的样本编号是：" + samplecode)
    #开始上传
    type_info, upload_args = get_config_info(config)
    result = upload_report(samplecode, upload_args)
    return render(request, 'execute.html', {'samplecode':samplecode,'result': result})
