class CQueue:
	def __init__(self,MAX):
		self.MAX=MAX
		self.queue=[None]*MAX
		self.front=self.rear=-1
	def isfull(self):
		if (self.rear+1)%self.MAX==self.front:
			return True
		else:
			return False
	def isempty(self):
		if (self.front==-1):
			return True
		else:
			return False
	def enqueue(self,item):
		if (self.isfull()):
			print("Queue is Full Currently!! Try Again Later!!")
		elif (self.front==-1):
			self.front=self.rear=0
			self.queue[self.rear]=item
		else:
			self.rear=(self.rear+1)%self.MAX
			self.queue[self.rear]=item
	def dequeue(self):
		if (self.isempty()):
			print("Queue is Empty!!")
		elif(self.front==0 and self.rear==0):
			pop=self.queue[self.front]
			print("Popped Element:",pop)
			self.front=self.rear=-1
		else:
			pop=self.queue[self.front]
			print("Popped Element:",pop)
			self.front=(self.front+1)%self.MAX
	def display(self):
		if (self.isempty()):
			print("Nothing to Display")
		elif (self.rear>=self.front):
			for i in range(self.front,self.rear+1):
				print(self.queue[i],end=" ")
			print()
		else:
			for i in range(self.front,self.MAX):
				print(self.queue[i], end=" ")
			for i in range(0,self.rear + 1):
				print(self.queue[i], end=" ")
			print()
			print("\nFront Element:",self.queue[self.front])
			print("\nRear Element:",self.queue[self.rear])
	def peek(self):
		print(self.queue[self.front])