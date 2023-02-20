from collections import Counter


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    def dfs(matching_word, words):

        nonlocal answer

        if not words:
            return 0

        matching_counter = Counter(matching_word)

        diff_dict = {}

        for word in words:

            word_counter = Counter(word)

            diff = matching_counter&word_counter

            diff_dict[word] = sum(diff.values())

            diff_dict = {k: v for k, v in diff_dict.items() if v == len(begin)-1}

        if target in diff_dict:
            answer += 1
            return answer

        print(diff_dict)
        # matched_word = [i for i,j in {k:v for k, v in diff_dict.items() if v == max(diff_dict.values())}.items()][0]
        matched_word = list(diff_dict.keys())[0]

        words.remove(matched_word)

        answer += 1

        dfs(matched_word, words)

    dfs(begin, words)

    return answer

    return dfs(begin, words, 0)
