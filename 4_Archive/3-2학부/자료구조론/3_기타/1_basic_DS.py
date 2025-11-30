# # 혼공실습 #1 : 10진수를 2진수로 바꾸는 클래스 만들기
# class dec_to_bin:
#     def __init__(self):
#         pass

#     def to_bin(self,dec): # 23
#         bin_list = []
#         while dec >= 1 :
#             bin_list.append(str(dec % 2))
#             dec = dec // 2
#         return ''.join(bin_list[::-1])
    
#     def to_dec(self,bin):
#         result = 0
#         j = 0
#         for i in str(bin)[::-1]:
#             print(int(i) * 2)
#             result += int(i) * (2 ** j)
#             j += 1
#         return result

# test1 = dec_to_bin()
# print(test1.to_bin(54))
# print(test1.to_dec(110110))

# # HW1 : 평균,표준편차,최대,최소 클래스
# class desc:
#     def __init__(self,num) :
#         self.num = num

#     def mean(self) :
#         return sum(self.num)/len(self.num)
    
#     def std(self) :
#         mean = desc(self.num).mean()
#         var_list = []
#         for i in self.num :
#             var_list.append((i - mean)**2)
#         var = desc(var_list).mean()
#         return var ** (1/2)

#     def max(self) :
#         return max(self.num)

#     def min(self) :
#         return min(self.num)

# test1 = desc([3,1,4,1])

# print(test1.std())




import matplotlib.pyplot as plt
import numpy as np

# Option parameters
k1_call_long = 100  # Long call strike price
c1_call_long = 5    # Long call premium
k2_call_short = 105 # Short call strike price
c2_call_short = 2   # Short call premium

# Stock price range at expiration
s_t = np.arange(80, 125, 1) # Stock price at expiration S_T

# Payoff calculation function (per share)
def bull_call_spread_payoff(s_t, k1_call_long, c1_call_long, k2_call_short, c2_call_short):
    # Value of options at expiration
    value_long_call_at_expiry = np.maximum(s_t - k1_call_long, 0)
    value_short_call_at_expiry = np.maximum(s_t - k2_call_short, 0)
    
    # Net premium paid (cost)
    net_premium_paid = c1_call_long - c2_call_short
    
    # Profit/Loss for the spread
    # P/L = Value of Long Call - Value of Short Call - Net Premium Paid
    payoff = value_long_call_at_expiry - value_short_call_at_expiry - net_premium_paid
    
    return payoff

# Calculate payoff
payoff = bull_call_spread_payoff(s_t, k1_call_long, c1_call_long, k2_call_short, c2_call_short)

# --- Create plot ---
plt.figure(figsize=(10, 6))

# Plot the spread payoff
plt.plot(s_t, payoff, label='Bull Call Spread P/L', color='blue', linewidth=2)

# Zero profit/loss line (breakeven line)
plt.axhline(0, color='black', linestyle='--', lw=1)

# Key points calculation
max_loss = -(c1_call_long - c2_call_short)
max_profit = (k2_call_short - k1_call_long) - (c1_call_long - c2_call_short)
breakeven_point = k1_call_long + (c1_call_long - c2_call_short)

# Plot key points on the graph
plt.plot(k1_call_long, max_loss, 'ro', markersize=7, label=f'K1 (Start of Max Loss) = ${k1_call_long}$')
plt.plot(k2_call_short, max_profit, 'go', markersize=7, label=f'K2 (Start of Max Profit) = ${k2_call_short}$')
plt.plot(breakeven_point, 0, 'yo', markersize=7, label=f'Breakeven Point = ${breakeven_point}$')

# Horizontal lines for max profit and max loss
plt.axhline(max_profit, color='green', linestyle=':', lw=1.5, label=f'Max Profit = ${max_profit:.2f}')
plt.axhline(max_loss, color='red', linestyle=':', lw=1.5, label=f'Max Loss = ${max_loss:.2f}')

# Graph titles and labels
plt.title('Bull Call Spread Payoff (Per Share)')
plt.xlabel('Stock Price at Expiration (S_T)')
plt.ylabel('Profit/Loss per Share ($)')

# Add legend and grid
plt.legend(loc='upper left')
plt.grid(True, linestyle='-', alpha=0.7)

# Adjust y-axis limits for better visualization
plt.ylim(payoff.min() - 1.5, payoff.max() + 1.5)
plt.xlim(s_t.min(), s_t.max())

# Show the plot (for local execution)
plt.show()