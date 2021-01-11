class Queue:
	def __init__(self,n1=5):
		self.queue=[]
		self.n=n1
		print("Functions Provided:\n\n1.)enqueue()\n2.)dequeue()\n3.)getpeek()\n\n")
		print("Default Max Queue Size:"+str(5))
		print("Max queue Size is:",n1)
	def isfull(self):
		if len(self.queue)==(self.n):
			return True
		else:
			return False
	def enqueue(self,item):
		if (self.isfull()):
			print("Max size Reached!!")
		else:
			self.queue.append(item)
			print("The element with Value:{} added to Queue.".format(item))
	def dequeue(self):
		if (self.isempty()):
			print("Nothing to Dequeue!!")
		else:
			item=self.queue.pop(0)
			print("The element with Value:{} Removed from Queue.".format(item))
			self.display()
	def isempty(self):
		if len(self.queue)==0:
			return True
		else:
			return False
	def display(self):
		if (self.isempty()):
			print("Nothing to Display!!")
		print(*self.queue)
	def getpeek(self):
		if (self.isempty()):
			print("Nothing to Display!!")
		else:
			print(self.queue[0])