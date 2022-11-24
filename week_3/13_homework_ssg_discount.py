# Q1. ✍️ 쓱 최대로 할인 적용하기
# Q.
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.
#
# [30000, 2000, 1500000] # 상품의 가격
# [20, 40]               # 쿠폰, 할인율의 단위는 % 입니다.

# => 가장 높은 가격에게 가장 높은 할인율을 적용해야 하지 않을까?
# => 그 다음으로 놓은 가격에게 그 다음으로 높은 할인 쿠폰을 적용하고.
# => 쿠폰이 다 없어지면 남은 가격들을 단순히 더하고.

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# 내 버전:
def get_max_discounted_price1(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    sum = 0
    for i in range(len(prices)):
        if i < len(coupons):
            sum += prices[i] * (1 - (coupons[i] / 100.0))
        else:
            sum += prices[i]
    return int(sum)


print(get_max_discounted_price1(shop_prices, user_coupons))  # 926000 이 나와야 합니다.


# 강의판 해답: (내 버전이 훨씬 나은 것 같다)(다 보지 않음. 괜히 복잡하게 생겨서...)
def get_max_discounted_price2(prices, coupons):
    coupons.sort(reverse=True)
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price1([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price1([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price1([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price1([20000, 100000, 1500000], [10, 10, 10]))