from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_isca/', views.about_isca, name='about_isca'),
    path('schedule_2019/', views.schedule_2019, name='schedule_2019'),
]

# 품질시스템
urlpatterns += [
    path('ISO_9001_요구사항/', views.ISO_9001_요구사항, name='ISO_9001_요구사항'),
    path('ISO_9001_내부심사원양성/', views.ISO_9001_내부심사원양성, name='ISO_9001_내부심사원양성'),
]

# 환경시스템
urlpatterns += [
    path('ISO_14001_요구사항/', views.ISO_14001_요구사항, name='ISO_14001_요구사항'),
    path('ISO_14001_내부심사원양성/', views.ISO_14001_내부심사원양성, name='ISO_14001_내부심사원양성'),
]

# 안전보건 경영시스템
urlpatterns += [
    path('ISO_45001_2018_제정_시스템전환실무/', views.ISO_45001_2018_제정_시스템전환실무, name='ISO_45001_2018_제정_시스템전환실무'),
    path('ISO_45001_실무및내부심사원양성/', views.ISO_45001_실무및내부심사원양성, name='ISO_45001_실무및내부심사원양성'),
]

# 자동차 산업경영시스템
urlpatterns += [
    path('자동차부품제조업_고객요구사항_이해및적용/', views.자동차부품제조업_고객요구사항_이해및적용, name='자동차부품제조업_고객요구사항_이해및적용'),
    path('IATF16949_2016_요구사항_이해와적용/', views.IATF16949_2016_요구사항_이해와적용, name='IATF16949_2016_요구사항_이해와적용'),
    path('IATF16949_2016_내부심사원_양성/', views.IATF16949_2016_내부심사원_양성, name='IATF16949_2016_내부심사원_양성'),
    path('품질환경_통합_내부심사원양성/', views.품질환경_통합_내부심사원양성, name='품질환경_통합_내부심사원양성'),
    path('품질안전보건_통합_내부심사원양성/', views.품질안전보건_통합_내부심사원양성, name='품질안전보건_통합_내부심사원양성'),
    path('품질환경안전_통합_내부심사원양성/', views.품질환경안전_통합_내부심사원양성, name='품질환경안전_통합_내부심사원양성'),
]

# 핵심부속서(CORE TOOl)
urlpatterns += [
    path('CORE_TOOL_이해와_실무적용/', views.CORE_TOOL_이해와_실무적용, name='CORE_TOOL_이해와_실무적용'),
    path('APQP_이해와_실무적용/', views.APQP_이해와_실무적용, name='APQP_이해와_실무적용'),
    path('FMEA_이해와_실무적용/', views.FMEA_이해와_실무적용, name='FMEA_이해와_실무적용'),
    path('APQP_FMEA_이해와_실무적용/', views.APQP_FMEA_이해와_실무적용, name='APQP_FMEA_이해와_실무적용'),
    path('MSA_이해와_실무적용/', views.MSA_이해와_실무적용, name='MSA_이해와_실무적용'),
]