1. установка qemu
   `sudo apt install qemu-kvm libvirt-clients libvirt-daemon-system virtinst bridge-utils virt-manager`
2. перейти в директорию, где лежит скаченный образ, устанавливаемой системы
3. Создаем виртуальную машину объемом 30gb
   `qemu-img create -f qcow2 mint_22_3.qcow2 30G`
4. Устанавливаем ОС (в данном случае linux mint 22.3)
   `qemu-system-x86_64 -enable-kvm -smp 6 -m 4096 -hda /home/che/Downloads/mint_22_3.qcow2 -boot d -cdrom /home/che/Downloads/linuxmint-22.3-cinnamon-64bit.iso`
5. Запускаем виртуальную машину
   `qemu-system-x86_64 -hda /home/che/Downloads/mint_22_3.qcow2  -m 4048 -cpu host -enable-kvm -net user,hostfwd=tcp::10022-:22 -net nic`
   `qemu-system-x86_64 -hda /home/che/Downloads/mint_22_3.qcow2  -m 4048 -smp 4 -enable-kvm -net user,hostfwd=tcp::10022-:22 -net nic`
