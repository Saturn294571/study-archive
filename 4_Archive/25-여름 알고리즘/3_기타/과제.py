# ROI(투자수익률) 순으로 정렬하는 병합 정렬(merge_sort) 재귀 함수
def merge_sort(assets):
    # 리스트의 원소가 1개 이하면 이미 정렬된 상태이므로 그대로 반환
    if len(assets) <= 1:
        return assets

    # 1. 분할
    mid = len(assets) // 2
    # 재귀 호출을 통해 왼쪽과 오른쪽 리스트를 각각 정렬
    left_half = merge_sort(assets[:mid])
    right_half = merge_sort(assets[mid:])

    # 2. 정복(병합)
    merged = []
    i, j = 0, 0
    # 두 리스트를 비교하며 ROI가 높은 순서로 정렬
    while i < len(left_half) and j < len(right_half):
        if left_half[i]['roi'] >= right_half[j]['roi']:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
            
    # 남아있는 요소들을 결과에 추가
    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    
    return merged

# 분할 가능 배낭문제를 적용한 그리디 포트폴리오 최적화 함수
def fractional_knapsack_optimizer(assets, budget):

    # 1. 각 자산의 투자수익률(ROI) 계산하여 추가
    for asset in assets:
        if asset['cost'] > 0:
            asset['roi'] = asset['expected_return'] / asset['cost']
        else:
            asset['roi'] = 0

    # 2. ROI를 기준으로 자산을 내림차순 정렬 (병합 정렬 함수 사용)
    sorted_assets = merge_sort(assets)

    # 포트폴리오 구성
    portfolio = []
    total_return = 0
    remaining_budget = budget

    print("--- 투자 결정 과정 ---")
    # 3. 정렬된 자산을 순회하며 포트폴리오에 추가
    for asset in sorted_assets:
        print(f"고려 자산: {asset['name']} (비용: {asset['cost']}, 수익률: {asset['roi']:.2f})")
        
        # 예산이 남아있지 않으면 즉시 종료
        if remaining_budget == 0:
            print(" -> 예산 모두 소진. 투자 종료.")
            break

        # 전체 자산을 담을 예산이 충분한 경우
        if remaining_budget >= asset['cost']:
            portfolio.append({'name': asset['name'], 'invested_cost': asset['cost'], 'proportion': 1.0})
            total_return += asset['expected_return']
            remaining_budget -= asset['cost']
            print(f"  -> 전체 편입 결정 (남은 예산: {remaining_budget})")
        
        # 예산이 부족하여 전체를 담을 수 없는 경우 -> 남은 예산만큼 분할하여 투자
        else:
            fraction = remaining_budget / asset['cost']
            invested_cost = asset['cost'] * fraction
            fractional_return = asset['expected_return'] * fraction
            
            portfolio.append({'name': asset['name'], 'invested_cost': invested_cost, 'proportion': fraction})
            total_return += fractional_return
            remaining_budget = 0 # 남은 예산을 모두 사용
            
            print(f"  -> 부분 편입 결정 ({fraction*100:.1f}% 만큼 편입, 남은 예산: {remaining_budget})")

    return portfolio, total_return, budget - remaining_budget

# 실행 예시
# 투자 가능한 자산 목록
investment_assets = [
    {'name': '프로젝트 A', 'cost': 3100, 'expected_return': 1400},
    {'name': '프로젝트 B', 'cost': 4100, 'expected_return': 1400},
    {'name': '프로젝트 C', 'cost': 5900, 'expected_return': 2100},
    {'name': '프로젝트 D', 'cost': 6500, 'expected_return': 3500},
    {'name': '프로젝트 E', 'cost': 3500, 'expected_return': 620}
]

# 총 투자 예산
total_budget = 15000

# 최적화 함수 실행
selected_portfolio, expected_value, invested_amount = fractional_knapsack_optimizer(investment_assets, total_budget)

print("\n--- 최종 포트폴리오 ---")
print("선택된 자산 내역:")
for item in selected_portfolio:
    print(f"  - {item['name']}: {item['invested_cost']:,.0f}원 투자 ({item['proportion']*100:.1f}% 편입)")

print(f"\n총 투자 비용: {invested_amount:,.0f}원")
print(f"총 기대 수익: {expected_value:,.2f}")