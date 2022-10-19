try:
    import numpy
except ImportError:
    print("numpy 模块未安装")
else:
    print("numpy 模块已安装")
try:
    import matplotlib
except ImportError:
    print("matplotlib 模块未安装")
else:
    print("matplotlib 模块已安装")
try:
    import pandas
except ImportError:
    print("pandas 模块未安装")
else:
    print("pandas 模块已安装")
try:
    np = numpy
    mpl = matplotlib
    pd = pandas
except ModuleNotFoundError:
    print("请尝试再次安装")
input("Press Enter to exit... ")
