#!usr/bin/python3

def reorderLogFiles(logs: list[str]) -> list[str]:
    letter_log, digit_log = [], []

    for i,log in enumerate(logs):
        logSplit = log.split(' ',1)

        if logSplit[1][0].isdigit():
            digit_log.append(log)
        else:
            letter_log.append([logSplit[1],logSplit[0],i])
    res = []
    for log in sorted(letter_log):
        res.append(logs[log[2]])
    
    return res+digit_log

if __name__ == "__main__":
    print(reorderLogFiles(logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))