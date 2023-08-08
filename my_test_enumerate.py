# fruit_list=["苹果","香蕉"]
# for index,fruit in enumerate(fruit_list):
#     print(f"The {index+1} fruit is {fruit}")

# print(fruit_list[:2])



def read_file_in_batches(input_file_path, output_file_path,batch_size=400):
    batch = []
    with open(input_file_path, 'r',encoding="utf8") as file:
        for line_number, line in enumerate(file, 1):
            batch.append(line.strip())
            if line_number % batch_size == 0:
                with open(output_file_path, 'a+',encoding="utf8") as output_file:
                    output_file.write("\n".join(batch))
                print(f"Batch {line_number // batch_size}:")
                print(batch)
                batch = []


# 读取文件并每100行为一组存储到数组
input_file_path = "D:\\Github\\deepl-translate\\ABOCADETS_content.txt"
output_file_path = "D:\\Github\\deepl-translate\\outputfile.txt"
read_file_in_batches(input_file_path,output_file_path )