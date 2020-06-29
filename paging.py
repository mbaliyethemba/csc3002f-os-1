#SHNMBA004
#Mbaliyethemba Shangase
#OS Assignment 1
#10 April 2019

from random import randint
import sys

#FIFO
def FIFO(size,pages):
  frames=[]
  page_fault=0
  for i in range(size):
    frames.append(-1)
  marker=0
  i=0
  while(marker!=size and i<len(pages)):
    if (pages[i] not in frames):
      frames[marker]= pages[i]
      marker+=1
      page_fault+=1
    i+=1
  marker=0
  for i in range(i,len(pages)):
    if(pages[i] not in frames):
      page_fault+=1
      frames[marker]=pages[i]
      marker=(marker+1)%size
  frames=[]
  return page_fault

#LRU
def LRU(size,pages):
  frames=[]
  page_fault=0
  for i in range(size):
    frames.append(-1)
  marker=0
  i=0
  while(marker!=size and i<len(pages)):
    if (pages[i] not in frames):
      frames[marker]=pages[i]
      marker+=1
      page_fault+=1
    i+=1
  while(i<len(pages)):
    if(pages[i] not in frames):
      least=-1
      ret_val=-1
      for j in range(size):
        x=pages[i::-1].index(pages[j])
        if(x>least):
          least=x
          ret_val=frames[j]
      x=frames.index(ret_val)
      frames[x]=pages[i]
      page_fault+=1
    i+=1
  frames=[]
  return page_fault
  
#OPT
def OPT(size,pages):
  frames=[]
  for i in range(size):
    frames.append(-1)
    page_fault,marker,i=0,0,0
  while(marker!=size and i<len(pages)):
    if (pages[i] not in frames):
      frames[marker]=pages[i]
      marker+=1
      page_fault+=1
    i+=1
  while(i<len(pages)):
    if(pages[i] not in frames):
      value=find_opt(size,pages,i)
      frames[value]=pages[i]
      page_fault+=1
    i+=1
  frames=[]  
  return page_fault
  
#Optimal page selection
def find_opt(size,pages,i):
  frames=[]
  for i in range(size):
    frames.append(0)
  ret_val,last,temp=-1,-1,-1
  for j in range(size):
    if frames[j] in pages[i:]:
      frames[j]=1
      temp=pages[i:].index(frames[j])
    if temp>last:
      last=temp
      ret_val=j
  if frames.count(1)==0:
    return 0
  elif frames.count(1)==1:
    x=frames.index(1)
    if(x==0):
      return 1
    else:
      return 0
  elif frames.count(1)>1 and frames.count(1)<size-1:
    x=frames.index(0)
    return x
  elif frames.count(1)==size-1:
    x=frames.index(0)
    return x
  else:
    return ret_val
    
def main():
	pages=[]
	size = int(sys.argv[1])
	for i in range(32):  #reference string random generation
		pages.append(randint(0,9))	
	print ("FIFO", FIFO(size,pages), "page faults.")
	print ("LRU", LRU(size,pages), "page faults.")
	print ("OPT", OPT(size,pages), "page faults.")
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Usage: python paging.py [number of pages]")
	else:
		main() 
