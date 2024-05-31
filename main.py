from flask import Flask, render_template ,request, jsonify
from db.create import createTables , createUser
from db.getUsers import getAllUsers, getSpecificUser
from db.create import createTables , createUser
from db.userOperation import isApproved,isBlocked
from db.product import createProduct,updateStockStatus, updateProductPrice
from db.level import updateUserLevel
from db.getProduct import getAllProducts,getSpecificProduct




app =Flask(__name__)




        #DEFAULT------ROUTE

@app.route('/', methods=['GET'])
def default():
   return "Hello World!"







        #CREATE--------------USER 

@app.route('/createUser', methods=['POST'])
def create_user():
    name = request.form.get('name')
    password = request.form.get('password')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    pinCode = request.form.get('pinCode')

    if not all([name, password, phone, email, address, pinCode]):
        return jsonify({'success': 400, 'message': 'Missing required fields. Please provide all fields.'})

    success = createUser(name=name, password=password, phone=phone, email=email, address=address, pinCode=pinCode)

    if success:
        return jsonify({'success': 200, 'message': 'Data Inserted Successfully!'})
    else:
        return jsonify({'success': 400, 'message': 'Failed to Insert Data'})





                
        #GET-------ALL-----USER

@app.route("/getAllUser",methods=['GET'])
def getAllUser():
    return getAllUsers()




        #GET-----SPECIFIC-----USER

@app.route("/getUser",methods=['GET'])
def getUser():
    userID= request.form['userID']
    return getSpecificUser(userId=str(userID))






        #UPDATE----USER-----LEVEL

@app.route('/updateUserLevel', methods=['PATCH'])
def update_UserLevelHandler():
    userId = request.form.get('ID')
    level = request.form.get('level')
    if not userId or not level:
        return jsonify({'success': 400, 'message': 'Missing ID or level in request'})
    
    success = updateUserLevel(id=userId, level=level)
    if success:
        return jsonify({'success': 200, 'message': 'User Level Updated Successfully!'})
    else:
        return jsonify({'success': 400, 'message': 'Failed to Update the User Level'})







        #APPROVE------USER

@app.route('/isApproved', methods=['PATCH'])
def user_Aproved():
    userId = request.form.get('ID')
    approved = request.form.get('approved')

    if not all([userId, approved]):
        return jsonify({'success': 400, 'message': 'Missing required fields. Please provide both ID and approved status.'})

    success = isApproved(id=userId, approved=approved)
    if success:
        return jsonify({'success': 200, 'message': 'User Approved Successfully!'})
    else:
            return jsonify({'success': 400, 'message': 'Failed! to Approve User'})
    





        #BLOCK------USER
    
@app.route('/isBlocked', methods=['PATCH'])
def user_Blocked():
    userId= request.form.get('ID')
    blocked= request.form.get('blocked')
    if not all([userId, blocked]):
        return jsonify({'success': 400, 'message': 'Missing required fields. Please provide both ID and blocked status.'})

    success=isBlocked(id=userId,blocked=blocked)
    if success:
            return jsonify({'success': 200, 'message': 'User Blocked Successfully!'})
    else:
            return jsonify({'success': 400, 'message': 'Failed! to Blocked User'})







        #CREATE-----PRODUCT

@app.route('/createProduct', methods=['POST'])
def create_product():

        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')
        stock = request.form.get('stock')
        isActive = request.form.get('isActive')
        if not all([name,price,category,stock,isActive]):
            return jsonify({'success': 400, 'message': 'Missing required fields. Please provide all fields.'})

        success = createProduct(name, price, category, stock, isActive)
        if success:
            return jsonify({'success': 200, 'message': 'Product created successfully!'})
        else:
            return jsonify({'success': 400, 'message': 'Failed to create product'})
        





        #GET-----ALL-----PRODUCTS

@app.route("/getAllProducts",methods=['GET'])
def getAllProduct():
    return getAllProducts()
        






        
        #GET-----SPECIFIC----PRODUCT

@app.route("/getProduct",methods=['GET'])
def getproduct():
    productID= request.form.get('ID')
    return getSpecificProduct(productId=str(productID))







        #UPDATE------PRRODUCT(stock--&--status)

@app.route('/updateProduct', methods=['PATCH'])
def update_Product():
    id = request.form.get('ID')
    stock = request.form.get('stock')
    isActive = request.form.get('isActive')
    if not all([id,stock,isActive]):
            return jsonify({'success': 400, 'message': 'Missing required fields. Please provide all fields.'})
    success=updateStockStatus(id=id, stock=stock, isActive=isActive)
    if success:
            return jsonify({'success': 200, 'message': 'Product Updated Succesfully!'})
    else:
            return jsonify({'success': 400, 'message': 'Failed! Update the Product'})



                


    #UPDATE----PRODUCT----PRICE

@app.route('/updateProductPrice', methods=['PATCH'])
def update_ProductPrice():
    id = request.form.get('ID')
    price = request.form.get('price')
    if not all([id, price]):
        return jsonify({'success': 400, 'message': 'Missing required fields. Please provide both id and price values correctly.'})
    success=updateProductPrice(id=id, price=price)
    if success:
            return jsonify({'success': 200, 'message': 'Product Price Updated Succesfully!'})
    else:
            return jsonify({'success': 400, 'message': 'Failed! Update the Price of Product'})




if __name__ == '__main__':
    createTables()
    app.run()  