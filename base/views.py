from django.shortcuts import render


def index(request):
    return render(request, 'base/index.html')

def about_isca(request):
    return render(request, 'base/about_isca.html')

def schedule_2019(request):
    return render(request, 'base/schedule_2019.html')


# 품질시스템
def ISO_9001_요구사항(request):
    return render(request, 'base/ISO_9001_요구사항.html')

def ISO_9001_내부심사원양성(request):
    return render(request, 'base/ISO_9001_내부심사원양성.html')


# 환경시스템 
def ISO_14001_요구사항(request):
    return render(request, 'base/ISO_14001_요구사항.html')

def ISO_14001_내부심사원양성(request):
    return render(request, 'base/ISO_14001_내부심사원양성.html')


# 안전보건 경영시스템
def ISO_45001_2018_제정_시스템전환실무(request):
    return render(request, 'base/ISO_45001_2018_제정_시스템전환실무.html')

def ISO_45001_실무및내부심사원양성(request):
    return render(request, 'base/ISO_45001_실무및내부심사원양성.html')


# 자동차 산업경영시스템

def 자동차부품제조업_고객요구사항_이해및적용(request):
    return render(request, 'base/자동차부품제조업_고객요구사항_이해및적용.html')

def IATF16949_2016_요구사항_이해와적용(request):
    return render(request, 'base/IATF16949_2016_요구사항_이해와적용.html')

def IATF16949_2016_내부심사원_양성(request):
    return render(request, 'base/IATF16949_2016_내부심사원_양성.html')

def 품질환경_통합_내부심사원양성(request):
    return render(request, 'base/품질환경_통합_내부심사원양성.html')

def 품질안전보건_통합_내부심사원양성(request):
    return render(request, 'base/품질안전보건_통합_내부심사원양성.html')
    
def 품질환경안전_통합_내부심사원양성(request):
    return render(request, 'base/품질환경안전_통합_내부심사원양성.html')


# 핵심부속서(CORE TOOL)

def CORE_TOOL_이해와_실무적용(request):
    return render(request, 'base/CORE_TOOL_이해와_실무적용.html')

def APQP_이해와_실무적용(request):
    return render(request, 'base/APQP_이해와_실무적용.html')

def FMEA_이해와_실무적용(request):
    return render(request, 'base/FMEA_이해와_실무적용.html')

def APQP_FMEA_이해와_실무적용(request):
    return render(request, 'base/APQP_FMEA_이해와_실무적용.html')
    
def MSA_이해와_실무적용(request):
    return render(request, 'base/MSA_이해와_실무적용.html')