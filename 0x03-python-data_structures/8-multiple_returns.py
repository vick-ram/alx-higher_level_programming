#!/usr/bin/python3
if __name__ == "__main__":
    def multiple_returns(sentence):
        if not sentence:
            return (0, None)
	return (len(sentence), sentence[0])
