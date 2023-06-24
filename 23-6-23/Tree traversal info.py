tree traversal types:
    1.level order traversal:
        you would traverse level by level left to right.
    2.depth first traversal:
        1.inorder(left,data,right)
        2.preorder(data,left,right)
        3.postorder(left,right,data)

         100
         /  \
       400  500
     /  \   /  \
   700 600 800 200

inorder:700 400 600 100 800 500 200
preorder:100 400 700 600 500 800 200
postorder:700 600 400 800 200 500 100
