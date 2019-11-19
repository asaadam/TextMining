class Test:
    @staticmethod
    def main():
        num_list = [(151258350, 2464),
                    (151258350, 56),
                    (151262958, 56),
                    (151258350, 56),
                    (151262958, 112),
                    (151262958, 112),
                    (151259627, 56),
                    (151262958, 112),
                    (151262958, 56)]
        num_dict = {}
        for t in num_list:
            if t[0] in num_dict:
                print(t[0])
                num_dict[t[0]] = num_dict[t[0]] + t[1]
            else:
                num_dict[t[0]] = t[1]
        #
        # for key, value in num_dict.items():
        #     print  (key, value)

Test.main()