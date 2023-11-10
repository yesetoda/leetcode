from collections import Counter
class Solution:
    def beautySum( s: str) -> int:
        total_beauty = 0
        length = len(s)

        for i in range(length):
            char_counts = [0] * 26  # To store the frequency of each lowercase English letter

            for j in range(i, length):
                char_counts[ord(s[j]) - ord('a')] += 1
                max_count = max(char_counts)
                min_count = min(count for count in char_counts if count > 0)

                total_beauty += max_count - min_count

        return total_beauty
    print(beautySum(s = "vptkmayimrtajqchkxurytfelwyelaworbgifjbuxxrfphhljnyfpsmtzbfgiqduuqeupsfwxklywzwpfjwhjikcxfmzxaiteznibsjkudtanucwralzpenggjfnoifwbuemuqnrlorfnqjhpsktifqazuiivislyavchbabtigtopfpnxaakpowfoperzleejcodgmaktdshbtqdbvlixkigrkpxzgmzsuduzvrbiwznmjoyqrmvybbybgkhhpgqykuislnxpfzqoempnpaehixuubrjomckaiftqrfprhfjnzmiocqcjjhosrvrntrjqfxtycjhoolfgosuqabtzunuaayqpzhygmsctzfoysvczowiudjxktztrmlbvvnhtznlzqfajkmwpborcizdrdalqxppsxmrhmtpyzbuovjtryenkgvabnhssapdoereptsyqxbvvnatharyjhxqmvvbcwllejowivjhzqqjukaagjyzdzj"))
# from random import choice
# alpha = 'qwertyuiopasdfghjklzxcvbnm'
# print(''.join([choice(alpha) for i in range(500)]))