##import pymysql as p
##
##while True:
##    con=p.connect(user="root",password="sushank",host="localhost",database="testdb")
##    cur=con.cursor()
##    query="select * from product"
##    cur.execute(query)
##    data=cur.fetchall()
##    for i in data:
##        print("")
##        print("product id :",i[0])
##        print("product name :",i[1])
##        print("product cost :",i[2])
##        print("product stock :",i[3])
##        print("--------------------")
##    con.commit()
##    con.close()
##
##
##    choice=int(input("1:buy \n2:generete bill\n3:exit\n"))
##    if choice == 1:
##        product_id=int(input("enter product id :"))
##        quantity=int(input("enter quantity :"))
##        con=p.connect(user="root",password="sushank",host="localhost",database="testdb")
##        cur=con.cursor()
##        query=f"update product set stock=stock-{quantity} where pid={product_id} "
##        query1=f"insert into cart(pname,stock,cost) select pname,{quantity},cost from product where pid={product_id}"
##        cur.execute(query)
##        cur.execute(query1)
##        print("\nproduct buy successfully")
##        print("************************")
##        con.commit()
##        con.close()
##
##    elif choice==2:
##        print("****** bill ******")
##        con=p.connect(user="root",password="sushank",host="localhost",database="testdb")
##        cur=con.cursor()
##        query="select sum(cost*stock) as amount from cart"
##        cur.execute(query)
##        data=cur.fetchall()
##        for i in data:
##            print("total bill =",i[0])
##            print("-------------------")
##        con.commit
##        con.close
##
##    elif choice==3:
##        break



#######################################

import pymysql as p

while True:
    con=p.connect(user="root",password="sushank",host="localhost",database="testdb")
    cur=con.cursor()
    query="select * from product"
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print()
        print("product id :",i[0])
        print("product name :",i[1])
        print("product cost :",i[2])
        print("product stock :",i[3])
        print("-----------------")
    con.commit()
    con.close()

    choice=int(input("1:buy \n2:generete bill\n3:show cart\n4:exit\n"))
    if choice == 1:
        product_id=int(input("enter product id :"))
        quantity=int(input("enter quantity :"))
        con=p.connect(user="root",password="sushank",host="localhost",database="testdb")
        cur=con.cursor()
        query=f"update product set stock=stock-{quantity} where pid={product_id} "
        query1=f"insert into cart(pname,stock,cost) select pname,{quantity},cost from product where pid={product_id}"
        cur.execute(query)
        cur.execute(query1)
        con.commit()
        con.close()

    elif choice==2:
        print("generate bill")
        con=p.connect(user="root",password="sushank",host="localhost",database="testdb")
        cur=con.cursor()
        query="select sum(cost*stock) as amount from cart"
        cur.execute(query)
        data=cur.fetchall()
        for i in data:
            print("total bill =",i[0])
        con.commit
        con.close

    elif choice==3:
        print("**** cart ****")
        con=p.connect(user="root",password="sushank",host="localhost",database="testdb")
        cur=con.cursor()
        query="select * from cart"
        cur.execute(query)
        data=cur.fetchall()
        for i in data:
            print("")
            print("product name =",i[0])
            print("product quantity =",i[1])
            print("-------------------------\n")
        con.commit()
        con.close()















