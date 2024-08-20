from packaging import version

if __name__ == "__main__":
    v1 = version.parse('7.8.0')
    v2 = version.parse('7.8.0+20202292009_001')

    if v1 > v2:
        print("v1 > vv2")
    elif v1 < v2:
        print("v1 < v2")
    else:
        print('v1 = v2')
