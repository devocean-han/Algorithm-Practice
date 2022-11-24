# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가
# ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가
# ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
#
# menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
# orders = ["오뎅", "콜라", "만두"]

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"] #, "튀김"]


# 방법 1: 단순히 전체 '주문받은 메뉴'를 돌며 있고 없고 체크하기 -> 시간 복잡도 O(N)
def is_available_to_order1(menus, orders):
    for item in orders:
        if item not in menus:
            return False
    return True


# 방법 2: 정렬 후 이진 탐색 -> 시간 복잡도 O((N + M) * logN) => N^2 다음으로 오래 걸리는 복잡도!
# 정렬 = O(N * logN)
# 주문 개수 M만큼 이진 탐색 반복 = O(M * logN)
# 따라서 둘을 더하면 위와 같은 시간 복잡도를 가지게 됨.
def is_available_to_order(menus, orders):
    menus.sort()  # menus 정렬!
    for order in orders:
        if not is_existing_target_number_binary(order, menus):
            return False
    return True

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


# 방법 3: 집합(set)의 차 이용 -> 시간 복잡도 O(N + M)
# N개의 메뉴와 M개의 주문을 set으로 만들기 = O(N) + O(M)
# 따라서 위와 같은 시간 복잡도를 가짐.
# (참고로 집합 내에서 탐색에 걸리는 시간 복잡도는 O(1)이라고 한다)
def is_available_to_order3(menus, orders):
    return len(set(orders) - set(menus)) == 0


result = is_available_to_order3(shop_menus, shop_orders)
print(result)