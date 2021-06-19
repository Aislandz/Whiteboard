from tkinter import Tk,simpledialog,messagebox

print('WhiteFinder 白版 1.0——数据库系统')
root=Tk()
root.withdraw()
the_world ={}
database=simpledialog.askstring('WhiteFinder','请录入数据库:')

def read_from_file():
    with open(database) as file:
        for  line in file:
            line=line.rstrip('\n')
            country, city=line.split('/')
            the_world[country]=city

def write_to_file(country_name,city_name):
    with open(database,'a') as file:
        file.write(country_name+'/'+city_name+'\n')
        


read_from_file()

while True:
    query_country=simpledialog.askstring(database,'请输入项目:')

    if query_country in the_world:
        result=the_world[query_country]
        messagebox.showinfo('查询结果',
                                        '查询结果：'+query_country+'的结果为 '+result+'.')

    else:
        new_city=simpledialog.askstring('WhiteFinder录入',
                                                        '请输入'+query_country+'的结果：')
        the_world[query_country]=new_city
        write_to_file(query_country,new_city)
    
root.mainloop()
        
