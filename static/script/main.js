document.addEventListener("DOMContentLoaded", () => {
    var menu = document.querySelector('.menu');
    var close = document.querySelector('.close');
    var navbar = document.querySelector('.navbar-left');

    // Menu-ni bosganda navbar ko'rinadi
    menu.addEventListener('click', () => {
        navbar.style.display = "flex"; // Navbar ko'rinadi
        menu.style.display = "none"; // Menu-ni qayta ko'rsatish
        close.style.display = "block"; // Close-ni yashirish
        
    });
    
    // Close-ni bosganda navbar yashiriladi
    close.addEventListener('click', () => {
        navbar.style.display = "none"; // Navbar yashiriladi
        menu.style.display = "block"; // Menu-ni qayta ko'rsatish
        close.style.display = "none"; // Close-ni yashirish
    });




    function updateTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString();
        document.getElementById("time").textContent = timeString;
    }
    setInterval(updateTime, 1000);  // Har 1 soniyada yangilanadi





document.addEventListener('DOMContentLoaded', function () {
    // Viloyatni o'zgartirganda tumanlarni yangilash
    const regionSelect = document.getElementById('id_categoryRegion');
    const districtSelect = document.getElementById('districtSelect');

    if (regionSelect) {
        regionSelect.addEventListener('change', function () {
            const regionId = this.value; // Viloyatning ID-si

            // Tumanlarni tozalash
            districtSelect.innerHTML = '<option value="">Tuman tanlang</option>';

            if (regionId) {
                // AJAX so'rov yuborish
                fetch(`/get_districts/${regionId}/`)
                    .then(response => response.json())
                    .then(data => {
                        data.districts.forEach(district => {
                            const option = document.createElement('option');
                            option.value = district.id;
                            option.textContent = district.title;
                            districtSelect.appendChild(option); // Yangi tumanlarni qo'shish
                        });
                    })
                    .catch(error => console.error('Tumanlarni yuklashda xatolik:', error));
            }
        });
    }

    // IMEI form qo'shish
    const addImeiButton = document.getElementById('add_imei');
    const formsetTable = document.getElementById('imei_table');
    const totalForms = document.getElementById('id_imei_form-TOTAL_FORMS');

    if (addImeiButton) {
        addImeiButton.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value, 10); // Joriy formalar soni

            // Yangi qator yaratish
            const newRow = document.createElement('tr');
            newRow.className = 'imei-row mb-2';

            // IMEI input maydoni
            const imeiCell = document.createElement('td');
            const imeiInput = document.createElement('input');
            imeiInput.type = 'text';
            imeiInput.name = `imei_form-${formCount}-imei`;
            imeiInput.className = 'form-control';
            imeiInput.required = true;
            imeiCell.appendChild(imeiInput);

            // O'chirish tugmasi
            const deleteCell = document.createElement('td');
            const deleteButton = document.createElement('a');
            deleteButton.href = '#';
            deleteButton.className = 'delete-form btn btn-danger';
            deleteButton.innerHTML = '&times;';
            deleteCell.appendChild(deleteButton);

            // Yangi qatorni jadvalga qo'shish
            newRow.appendChild(imeiCell);
            newRow.appendChild(deleteCell);
            formsetTable.appendChild(newRow);

            // Formlar sonini yangilash
            totalForms.value = formCount + 1;
        });
    }

    // IMEI form o'chirish
    document.addEventListener('click', function (e) {
        if (e.target.closest('.delete-form')) {
            e.preventDefault();

            const row = e.target.closest('.imei-row'); // Qatorni aniqlash
            if (row) {
                row.remove(); // Qatorni o'chirish

                // Formlar sonini yangilash
                totalForms.value = parseInt(totalForms.value, 10) - 1;
            }
        }
    });
});

});