import sys
from scipy import spatial

reload(sys)
sys.setdefaultencoding('utf8')

topic_word = []
topic_word_weight = []
topic = []
topics = []
matrix_index = []
result_matrix = []


def main ():
    with open('../datas/medical_research/un_labeled/noun_lda-ef6e162e-18-6bad1c9f/01000/summary.txt') as f:
        lines = f.readlines()
        # print type(lines)
    with open('../datas/medical_research/pre_labeled/noun_llda-cvb0-a2389fde-3-bf4a9d4d-4b148d81/01000/summary.txt') as f1:
        lines2 = f1.readlines()

    for line in lines:
        # print type(line)
        # print line
        line = "".join(line.split("\n"))
        new_line = line.split('\t')
        # print new_line
        if len(new_line) == 3 and not new_line[0] == '':
            # print new_line[0]
            # print new_line[2]

            topic_weight = new_line[2]

        elif len(new_line) == 3 and new_line[0] == '':
            # print new_line
            # print new_line[1]
            # print new_line[2]
            topic_word.append(new_line[1])
            topic.append((new_line[1], float(new_line[2]) / float(topic_weight)))

    for line in lines2:
        # print type(line)
        # print line
        line = "".join(line.split("\n"))
        new_line = line.split('\t')
        # print new_line
        if len(new_line) == 3 and not new_line[0] == '':
            # print new_line[0]
            # print new_line[2]

            topic_weight = new_line[2]

        elif len(new_line) == 3 and new_line[0] == '':
            # print new_line
            # print new_line[1]
            # print new_line[2]
            topic_word.append(new_line[1])
            topic.append((new_line[1], float(new_line[2]) / float(topic_weight)))

    for i in range(0, 420, 20):
        topics.append(topic[i:i+20])


    for item in range(0, 21):
        # print item
        for word, weight in topics[item]:
            if word not in matrix_index:
                matrix_index.append(word)

    print len(matrix_index)

    for item in range(0, 21):
        temp_array = []
        for index in range(0, len(matrix_index)):
            temp_word = ''
            temp_weight = 0
            for word, weight in topics[item]:
                temp_word = matrix_index[index]
                if matrix_index[index] == word:
                    temp_weight = float(weight)
                    break
            temp_array.append(temp_weight)

        result_matrix.append(temp_array)
    print len(result_matrix)
    for row in result_matrix:
        print row
    for row in range(0, 18):
        similarity1 = 1 - spatial.distance.cosine(result_matrix[row], result_matrix[-1])
        similarity2 = 1 - spatial.distance.cosine(result_matrix[row], result_matrix[-2])
        similarity3 = 1 - spatial.distance.cosine(result_matrix[row], result_matrix[-3])
        print (similarity1, similarity2, similarity3)






if __name__ == "__main__":
	main()
