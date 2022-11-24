# Q3. ✍️ 멜론 베스트 앨범 뽑기
# Q.
# 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
#
# 노래는 인덱스로 구분하며, 노래를 수록하는 기준은 다음과 같다.
#
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의 재생 수 총합은 모두 다르다.)
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
#
# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
#
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.
#
# 예시 1:
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
# 정답 = [4, 1, 3, 0]

# 예시 2:
# genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
# plays = [2000, 500, 600, 150, 800, 2500, 2000]
# 정답 = [0, 6, 5, 2, 4, 1]

# => 가장 먼저 노래가 두 개 미만인 장르를 탈락시킨다(?)
# => 먼저 장르별 총 재생 횟수를 비교해야 한다. 총 재생이 높은 장르 순으로 돌면서...
# => hiphop, pop, classic 순서가 되겠지. 반복문을 그냥 주구장창 돌자...
# => 딕셔너리에 장르를 키로 집어넣으면 어떨까? 그래서 각 키마다 (인덱스, 재생수)
# => 이렇게 두 개의 값'들'이 들어가는 거다. 딱 아까 전에 했던 체이닝 충돌 해결 때처럼.
# => 딕셔너리의 '값'부분에 튜플을 요소로 가지는 리스트를 넣으면 되겠다.
# => 그러면 장르별 재생 총합 = 딕[hiphop]의 아이템별 [1]값들의 합
# => 장르 안에서 먼저 아이템별 재생 수 [1] 값 비교해서 더 큰 쪽의 [0](=인덱스)값을 최종 앨범에 먼저 넣기
# => [1]값의 top 2 값이 같으면 그냥 순서대로(인덱스를 비교해서?) [0](=인덱스)값을 최종 앨범에 넣기.
# => 그 다음 장르도 똑같이 진행하기.


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album1(genre_array, play_array):
    # 장르별로 {장르: [(인덱스, 재생수), (인덱스, 재생수)...]} 딕셔너리 만들기
    melon_dict = dict()
    for i in range(len(play_array)):
        if genre_array[i] not in melon_dict.keys():
            melon_dict[genre_array[i]] = [(i, play_array[i])]
        else:
            melon_dict[genre_array[i]].append((i, play_array[i]))
    print("melon_dict:", melon_dict)


    # 새 {장르: 총 재생수} 딕셔너리 만들기
    total_plays_per_genre = dict()
    for genre in melon_dict.keys():
        total_plays = sum(item[1] for item in melon_dict[genre])
        total_plays_per_genre[genre] = total_plays


    # {장르: 총 재생수} 딕셔너리를 재생수 내림차순으로 정렬
    total_plays_per_genre_sorted = {k: v for k, v
                                    in sorted(total_plays_per_genre.items(),
                                              key=lambda item: item[1],
                                              reverse=True)}
    # print(total_plays_per_genre_sorted)


    # 최종 앨범 리스트
    result_album = []

    # 재생수가 많은 장르부터 곡 선별 작업 시작
    for genre in total_plays_per_genre_sorted.keys():
        items = melon_dict[genre]
        # 장르 안의 곡들 재생수 내림차순 정렬하기...
        items.sort(key=lambda item: item[1], reverse=True)
        # print(f'"{genre}" items sorted:  {items}')
        if items[0][1] != items[1][1]:
            result_album.append(items[0][0])
            result_album.append(items[1][0])
        else:
            result_album.append(min(items[0][0], items[1][0]))
            result_album.append(max(items[0][0], items[1][0]))

    return result_album


# 강의판 해답:
def get_melon_best_album2(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
            # 근데 여기엔 '둘의 재생 수가 같은 경우, sorted되었을 때 기존의 순서가 유지되었을 거란 전제'
            # 를 기반으로 마치고 있다. 설명이 있어주면 더 좋았을 텐데.
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album2(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album2(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))



