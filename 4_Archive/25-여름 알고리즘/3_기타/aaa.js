class node {
    constructor(v,l,r){
        this.value = v;
        this.LChild = l;
        this.RChild = r;
    }

    print(content){
        console.log(content, this.value, this.LChild, this.RChild);
    }
}
aaa = [1,0,-1,'','a',[],{},(1,2),function(){}]
for (i=0;i<aaa.length;i++) {
    console.log(aaa[i], aaa[i] ? true : false)
}

myNode = new node(3,1,4)
myNode.LChild = 12
myNode.RChild = 3
myNode.value = 9

console.log(myNode)
myNode.print('aaaaaaaaaaaa')