#!/usr/bin/env python
# coding: utf-8

# In[5]:


nama = input("Masukkan nama lengkap Anda: ")
nim = input("Masukkan NIM Anda: ")
alamat = input("Masukkan alamat Anda: ")

print("=" * 30)
print("Biodata")
print("=" * 30)
print("Nama Lengkap:", nama)
print("NIM:", nim)
print("Alamat:", alamat)



# Tugas 2: Manipulasi kalimat
kalimat = "UNIVERSITAS NUSA PUTRA SUKABUMI"

# a. putra nusa
output_a = ' '.join(kalimat.split()[2:0:-1]).lower()
print("a. {}".format(output_a))

# b. NIVERSITAS NSA PTRA SKABMI
print("b. {}".format(kalimat.replace('U','')))

# c. SUKABUMI PUTRA NUSA UNIVERSITAS
kata = kalimat.split()
kata.reverse()
kalimat_balik = ' '.join(kata)
print("c. {}".format(kalimat_balik))

# d. UNPS
output_d = ''.join([word[0] for word in kalimat.split()])
print("d. {}".format(output_d))

# e. TAS SAPU BUMI
output_1 = (kalimat[8:11])
output_2 = (kalimat[14:16])
output_3 = (kalimat[17:19])
output_4 = (kalimat[-4:])
print("e. {}".format(output_1 +" "+output_2+output_3+" "+output_4))

