print("1.1 : khởi tạo list")
#list
list_user = ["Trí Hùng" , "Thiện Nhân" , "Thành Long"]
print(list_user)
list_user[0] = "lmao"
print(list_user)
print("1.2: khởi tạo tuple")
#tuple()
tuple_user = "việt dũng bé bỏng", "gia bảo đáng yêu", "đức thuy"
print(tuple_user)
tuple_user = "bủh"
print(tuple_user)
#code vẫn có thể chạy được khi ta tạo ra một tuple cùng tên thì code vẫn sẽ tính là tạo 1 code mới
tuple_age = 18, # gán dấu phẩy vào thì sẽ ra dữ liệu tuple nếu không thì sẽ ra dữ liệu của chính nó
print(type(tuple_age))
print("2.1:dictionary ")
#dùng dictionary giúp code tự ghi chép làm cho người đọc hiểu ngay từng trường dữ liệu đại diện cho thông tin
#ví dụ
"""student = {
"name": "Nguyễn Văn A",
"age": 18,
"grade": "Giói"

# Lấy tuổi + student["age"]
# hoặc sử dụng get
# Cực kỳ rõ ràng, không nham!

}"""
print("2.2 khởi tạo thử DICT ")
#init (khởi tạo
info_user = {
    "id_user": 1,
    "name_user": "Đông Thiên",
    "age": 20,
    "sex" : "male",
    "address" : {
        "id_adress" :1,
        "name_adress": "thanh hoa",
    },
    "is_status" : True,
    "year_exc": [1,1,2050],
    "res": "ca do"
}
#read(đọc)
#cách 1: sử dụng disc[key]
print("2.3 : cách 1")
print(f"{info_user['name_user']} đi bệnh viện vì {info_user['res']}")
#cách 2: .get("key")
print("2.4: cách 2")
print(f"{info_user.get("name_user_,","Đông Thiên")} {info_user.get("age")} tuổi")
# có thể truyền tham số mặc định vào trong giá trị để thay thế cho none của phương thức get(key)
# ví dụ truyền "đông thiên " vào để thay thế cho giá trị "name_user_," bị sai

#create
#Thêm thuộc tính số điện thoại vào trong dict info_user
print("2.5 thêm")
info_user["phone"] = "0123456789"
print(info_user["phone"])

#update
print("2.6: sửa")
info_user["phone"] = "0222222222"


#delete
print("2.7 xóa")
info_user.pop("res")
print(info_user)

#duyệt key 
print("3.1: duyệt qua key")
for keys in info_user.keys():
    print(f"key: {keys}")

#duyệt value
print("3.2: duyệt qua value")
for value in info_user.values():
    print(f"value: {value}")

#duyệt qua key : value
print("3.3: duyệt qua key : value")
for key, value in info_user.items():
    print(f"{key} | {value}")
