status = 'y'
switch = True

hasil = 0

while switch:
  n_barang = int(input("Entrikan jumlah barang yang dibeli: "))
  harga_barang = int(input("Entrikan harga satuan barangnya: "))
  hasil += (n_barang * harga_barang)
  status = input("Apakah ada lagi item barang yang dientrikan atau tidak? [y]/[t] ")
  while status != 'y' or status != 't':
    if status == "t":
      switch = False
      print(f"Total harga yang perlu dibayar adalah {hasil}")
      break
    elif status == "y":
      break
    else:
      print("Mohon maaf input yang anda masukkan salah")
      status = input("Apakah ada lagi item barang yang dientrikan atau tidak? [y]/[t] ")
struk = True
while struk:
  bayar = int(input("Masukkan uang tunai: "))
  kembalian = bayar - hasil
  while bayar >= hasil:
    struk = False
    print(f"\n===STRUK PEMBAYARAN=== \n\nTotal Harga: {hasil} \nUang Tunai: {bayar} \nKembalian: {kembalian}\n\n ***Terima kasih telah berbelanja***\n")
    break
  while bayar < hasil:
    print("Maaf Uang Tunai yang anda masukkan kurang")
    break
    