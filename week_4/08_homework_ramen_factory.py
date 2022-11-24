# Q1. ✍️ 농심 라면 공장
#
# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다. 원래 밀가루를 공급받던
# 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외
# 공장에서 밀가루를 수입해야 합니다.
#
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고,
# 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
#
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에
# 공급 가능한 밀가루 수량(supplies), 원래 공장으로부터 공급받을 수 있는 시점 k가
# 주어질 때, 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외
# 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.
#
# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는
# dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.
#
#
# 예시)
# stock = 4
# dates = [4, 10, 15]
# supplies = [20, 5, 10]
# k = 30
# 위와 같이 입력값이 들어온다면,
# 현재 재고가 4개 있습니다. 그리고 정상적으로 돌아오는 날은 30일까지입니다.
# 즉, 26개의 공급량을 사와야 합니다!
# 그러면 제일 최소한으로 26개를 가져오려면? supplies 에서 20, 10 을 가져오면 되겠죠?
# 그래서 이 경우의 최소 공급 횟수는 2 입니다!

# => dates중 k일을 넘어가는 날짜는 빼야겠다. 그 시점부터는 원래 공장에서 받을 수 있을 테니까.
# => 그러고 나서 k-stock 만큼의 숫자가 나오도록 supplies 중 최소한만 더하여 만드는 문제인데...
# => 예를 들어 4일째에 20톤을 받았다면 15일째까지 버텨서 10톤을 더 받는 게 가능하지만,
# => 만약 4일째에 10톤을 받았다면 15일째에 20톤을 받는 것은 불가능하다. 둘 다 합계는 30톤으로
# => 필요 수량인 26톤은 넘게 되지만...
# => ! 또 처음 받는 날짜는 stock을 넘어가면 안된다. 후...

# 힌트:
# import heapq
# heapq.heappush([], 4)
# heapq.heappop()
# 최대힙 만들려면 * -1 한 데이터를 넣어주고, 뺄 때 다시 * -1을 처리해주면 된다!



import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    return


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))