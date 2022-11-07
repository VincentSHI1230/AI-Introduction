try:
    import numpy
except ImportError:
    print("numpy 未安装")
else:
    print("numpy 已安装")
try:
    import scipy
except ImportError:
    print("scipy 未安装")
else:
    print("scipy 已安装")
try:
    import sklearn
except ImportError:
    print("scikit-learn 未安装")
else:
    print("scikit-learn 已安装")
try:
    np = numpy
    sp = scipy
    skl = sklearn
except ModuleNotFoundError:
    print("请尝试再次安装")
input("Press Enter to exit... ")
