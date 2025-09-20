import math

def tinh_hinh_tron():
    r = float(input("Nhập bán kính r: "))
    cv = 2 * math.pi * r
    dt = math.pi * (r ** 2)

    print(f"Chu vi hình tròn = {cv:.2f}")
    print(f"Diện tích hình tròn = {dt:.2f}")

if __name__ == "__main__":
    tinh_hinh_tron()
    
