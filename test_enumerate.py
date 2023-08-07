# fruit_list=["苹果","香蕉"]
# for index,fruit in enumerate(fruit_list):
#     print(f"The {index+1} fruit is {fruit}")

# print(fruit_list[:2])



def read_file_in_batches(file_path, batch_size):
    batch = []
    with open(file_path, 'r',encoding="utf8") as file:
        for line_number, line in enumerate(file, 1):
            batch.append(line.strip())
            if line_number % batch_size == 0:
                for i in range(3):
                    print("*"*50)
                print(f"Batch {line_number // batch_size}:")
                print(batch)
                batch = []
        # Print the last batch if it's not empty
        if batch:

            print(f"Batch {line_number // batch_size + 1}:")
            print(batch)

# 读取文件并每100行为一组存储到数组
file_path = "D:\\Github\\deepl-translate\\ABOCADETS_content.txt"
batch_size = 100
read_file_in_batches(file_path, batch_size)