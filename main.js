// Utility function to resolve image URL based on fallback config
function resolveImageUrl(src) {
    if (!src) return '';
    const lowercaseSrc = src.toLowerCase();
    if (src.startsWith('http') || src.startsWith('//') || src.startsWith('data:') || lowercaseSrc.startsWith('images/')) {
        // Rewrite local image references to match case of "Images/" directory
        if (lowercaseSrc.startsWith('images/')) {
            return 'Images/' + src.substring(7);
        }
        return src;
    }
    if (siteContent.config.useLiveImageFallback) {
        return siteContent.config.liveBaseUrl + src;
    }
    return src;
}

// Global Image Error handling / blank styling
function setElementImage(elementId, src, alt = '') {
    const el = document.getElementById(elementId);
    if (el) {
        el.src = resolveImageUrl(src);
        if (alt) el.alt = alt;
        el.onerror = function () {
            // Replaces image with a clean premium grey block
            el.style.display = 'none';
            const placeholder = document.createElement('div');
            placeholder.className = 'w-full h-full min-h-[160px] bg-slate-100 text-slate-400 flex flex-col items-center justify-center p-4 text-center rounded border border-slate-200';
            placeholder.innerHTML = `<i class="fa-regular fa-image text-3xl mb-2 text-slate-300"></i><span class="text-xs font-semibold uppercase tracking-wider">${alt || 'Image'}</span>`;
            el.parentNode.insertBefore(placeholder, el);
        };
    }
}

// Render Top Bar and Navigation Header
function renderHeader() {
    const topBar = document.getElementById('top-bar');
    if (topBar) {
        topBar.className = "bg-brandCyan text-white text-[14px] font-bold py-2.5 px-4 md:px-12 flex flex-col md:flex-row justify-between items-center z-50 relative gap-2";
        topBar.innerHTML = `
            <div class="flex flex-col sm:flex-row items-center gap-6">
                <a href="tel:${siteContent.header.phone}" class="flex items-center gap-1.5 hover:text-brandNavy transition-colors font-bold text-white">
                    <i class="fa-solid fa-mobile-alt"></i> ${siteContent.header.phone}
                </a>
                <a href="mailto:${siteContent.header.email}" class="flex items-center gap-1.5 hover:text-brandNavy transition-colors font-bold text-white">
                    <i class="fa-solid fa-envelope"></i> ${siteContent.header.email}
                </a>
            </div>
            <div class="w-full md:w-1/2 overflow-hidden relative">
                <marquee onmouseover="this.stop();" onmouseout="this.start();" scrollamount="4" class="font-bold text-center block text-white">
                    ${siteContent.header.marqueeDesktop}
                </marquee>
            </div>
        `;
    }

    const mainHeader = document.getElementById('main-header');
    if (mainHeader) {
        mainHeader.className = "bg-white relative z-40";

        // Active page extraction
        const path = window.location.pathname;
        const page = path.substring(path.lastIndexOf('/') + 1) || 'index.html';

        const isHome = page === 'index.html';
        const isAbout = page === 'about.html';
        const isAdmission = page === 'admission-process.html';
        const isFaculty = ['teaching-staff.html', 'non-teaching-staff.html'].includes(page);
        const isFacilities = page === 'facilities.html';
        const isCourses = ['b-pharm.html', 'd-pharm.html', 'b-sc.html', 'b-com.html', 'bca.html'].includes(page);
        const isAcademic = ['syllabus.html', 'academic-calendar.html', 'time-table.html'].includes(page);
        const isGallery = page === 'gallery.html';
        const isNews = page === 'news-events.html';
        const isContact = page === 'contact-us.html';

        mainHeader.innerHTML = `
            <!-- Centered Logo Area -->
            <div class="w-full bg-white py-4 flex justify-center items-center border-b border-slate-100">
                <a href="index.html" class="flex justify-center items-center">
                    <img id="header-logo-img" class="h-16 md:h-20 object-contain max-w-[90%] md:max-w-xl" alt="Arunodaya Institutions Logo">
                </a>
            </div>

            <!-- Navigation Menu Bar with Gradient -->
            <div class="w-full bg-gradient-to-r from-[#47ba7d] to-[#0158a5] shadow-lg sticky top-0">
                <div class="max-w-7xl mx-auto px-4 flex justify-between xl:justify-center items-center h-12">
                    <!-- Desktop Nav -->
                    <nav class="hidden xl:block w-full">
                        <ul class="flex justify-center items-center gap-1 text-[15px] font-extrabold text-white font-sans tracking-wide h-12">
                            <li class="relative h-full flex items-center">
                                <a href="index.html" class="px-5 h-full flex items-center transition-all ${isHome ? 'bg-brandBlue text-white' : 'hover:bg-brandBlue text-white'}">Home</a>
                            </li>
                            <li class="relative h-full flex items-center">
                                <a href="about.html" class="px-5 h-full flex items-center transition-all ${isAbout ? 'bg-brandBlue text-white' : 'hover:bg-brandBlue text-white'}">About Us</a>
                            </li>
                            <li class="relative h-full flex items-center">
                                <a href="admission-process.html" class="px-5 h-full flex items-center transition-all ${isAdmission ? 'bg-brandBlue text-white' : 'hover:bg-brandBlue text-white'}">Admission</a>
                            </li>
                            
                            <!-- Faculty Dropdown -->
                            <li class="dropdown relative h-full flex items-center cursor-pointer group">
                                <span class="px-5 h-full flex items-center transition-all gap-1.5 ${isFaculty ? 'bg-brandBlue text-white' : 'group-hover:bg-brandBlue text-white'}">
                                    Faculty <i class="fa-solid fa-angle-down text-xs"></i>
                                </span>
                                <ul class="dropdown-menu absolute left-0 top-12 w-48 bg-[#0c2b5c] text-white py-2 shadow-xl hidden group-hover:block z-50">
                                    <li><a href="teaching-staff.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">Teaching Staff</a></li>
                                    <li><a href="non-teaching-staff.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">Non-Teaching Staff</a></li>
                                </ul>
                            </li>

                            <li class="relative h-full flex items-center">
                                <a href="facilities.html" class="px-5 h-full flex items-center transition-all ${isFacilities ? 'bg-brandBlue text-white' : 'hover:bg-brandBlue text-white'}">Facilities</a>
                            </li>

                            <!-- Courses Dropdown -->
                            <li class="dropdown relative h-full flex items-center cursor-pointer group">
                                <span class="px-5 h-full flex items-center transition-all gap-1.5 ${isCourses ? 'bg-brandBlue text-white' : 'group-hover:bg-brandBlue text-white'}">
                                    Courses <i class="fa-solid fa-angle-down text-xs"></i>
                                </span>
                                <ul class="dropdown-menu absolute left-0 top-12 w-48 bg-[#0c2b5c] text-white py-2 shadow-xl hidden group-hover:block z-50">
                                    <li><a href="b-pharm.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">B. Pharm</a></li>
                                    <li><a href="d-pharm.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">D. Pharm</a></li>
                                    <li><a href="b-sc.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">B.Sc</a></li>
                                    <li><a href="b-com.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">B.Com</a></li>
                                    <li><a href="bca.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">BCA</a></li>
                                </ul>
                            </li>

                            <!-- Academic Dropdown -->
                            <li class="dropdown relative h-full flex items-center cursor-pointer group">
                                <span class="px-5 h-full flex items-center transition-all gap-1.5 ${isAcademic ? 'bg-brandBlue text-white' : 'group-hover:bg-brandBlue text-white'}">
                                    Academic <i class="fa-solid fa-angle-down text-xs"></i>
                                </span>
                                <ul class="dropdown-menu absolute left-0 top-12 w-48 bg-[#0c2b5c] text-white py-2 shadow-xl hidden group-hover:block z-50">
                                    <li><a href="syllabus.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">Syllabus</a></li>
                                    <li><a href="academic-calendar.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">Academic Calendar</a></li>
                                    <li><a href="time-table.html" class="block px-4 py-2.5 hover:bg-brandBlue hover:text-white transition-colors font-bold">Time Table</a></li>
                                </ul>
                            </li>

                            <li class="relative h-full flex items-center">
                                <a href="gallery.html" class="px-5 h-full flex items-center transition-all ${isGallery ? 'bg-brandBlue text-white' : 'hover:bg-brandBlue text-white'}">Gallery</a>
                            </li>
                            <li class="relative h-full flex items-center">
                                <a href="news-events.html" class="px-5 h-full flex items-center transition-all ${isNews ? 'bg-brandBlue text-white' : 'hover:bg-brandBlue text-white'}">News & Events</a>
                            </li>
                            <li class="relative h-full flex items-center">
                                <a href="contact-us.html" class="px-5 h-full flex items-center transition-all ${isContact ? 'bg-brandBlue text-white' : 'hover:bg-brandBlue text-white'}">Contact Us</a>
                            </li>
                        </ul>
                    </nav>

                    <!-- Mobile Menu Button -->
                    <button id="mobile-menu-btn" class="xl:hidden text-white text-3xl focus:outline-none ml-auto">
                        <i class="fa-solid fa-bars"></i>
                    </button>
                </div>
            </div>

            <!-- Mobile Drawer -->
            <div id="mobile-drawer" class="fixed inset-0 bg-[#0c2b5c] bg-opacity-95 text-white z-50 transform translate-x-full transition-transform duration-300 xl:hidden">
                <div class="flex justify-between items-center p-6 border-b border-slate-700">
                    <img id="mobile-logo-img" class="h-12 object-contain" alt="Arunodaya Logo">
                    <button id="mobile-menu-close" class="text-3xl"><i class="fa-solid fa-xmark"></i></button>
                </div>
                <div class="p-6 overflow-y-auto h-[calc(100vh-80px)]">
                    <ul class="flex flex-col gap-5 text-lg font-bold">
                        <li><a href="index.html" class="block py-1 hover:text-brandCyan transition-colors">Home</a></li>
                        <li><a href="about.html" class="block py-1 hover:text-brandCyan transition-colors">About Us</a></li>
                        <li><a href="admission-process.html" class="block py-1 hover:text-brandCyan transition-colors">Admission</a></li>
                        <li class="border-t border-slate-700 pt-3">
                            <span class="block text-slate-400 text-sm mb-2 uppercase tracking-widest font-semibold">Faculty</span>
                            <ul class="pl-4 flex flex-col gap-2 text-md">
                                <li><a href="teaching-staff.html" class="hover:text-brandCyan">Teaching Staff</a></li>
                                <li><a href="non-teaching-staff.html" class="hover:text-brandCyan">Non-Teaching Staff</a></li>
                            </ul>
                        </li>
                        <li><a href="facilities.html" class="block py-1 hover:text-brandCyan transition-colors">Facilities</a></li>
                        <li class="border-t border-slate-700 pt-3">
                            <span class="block text-slate-400 text-sm mb-2 uppercase tracking-widest font-semibold">Courses</span>
                            <ul class="pl-4 flex flex-col gap-2 text-md">
                                <li><a href="b-pharm.html" class="hover:text-brandCyan">B. Pharm</a></li>
                                <li><a href="d-pharm.html" class="hover:text-brandCyan">D. Pharm</a></li>
                                <li><a href="b-sc.html" class="hover:text-brandCyan">B.Sc</a></li>
                                <li><a href="b-com.html" class="hover:text-brandCyan">B.Com</a></li>
                                <li><a href="bca.html" class="hover:text-brandCyan">BCA</a></li>
                            </ul>
                        </li>
                        <li class="border-t border-slate-700 pt-3">
                            <span class="block text-slate-400 text-sm mb-2 uppercase tracking-widest font-semibold">Academic</span>
                            <ul class="pl-4 flex flex-col gap-2 text-md">
                                <li><a href="syllabus.html" class="hover:text-brandCyan">Syllabus</a></li>
                                <li><a href="academic-calendar.html" class="hover:text-brandCyan">Academic Calendar</a></li>
                                <li><a href="time-table.html" class="hover:text-brandCyan">Time Table</a></li>
                            </ul>
                        </li>
                        <li><a href="gallery.html" class="block py-1 hover:text-brandCyan transition-colors">Gallery</a></li>
                        <li><a href="news-events.html" class="block py-1 hover:text-brandCyan transition-colors">News & Events</a></li>
                        <li><a href="contact-us.html" class="block py-1 hover:text-brandCyan transition-colors">Contact Us</a></li>
                    </ul>
                </div>
            </div>
        `;

        // Bind Logo
        setElementImage('header-logo-img', siteContent.header.logoHeader, 'Arunodaya Logo');
        setElementImage('mobile-logo-img', siteContent.header.logoHeaderWhite, 'Arunodaya Logo');

        // Mobile Menu interactions
        const btn = document.getElementById('mobile-menu-btn');
        const drawer = document.getElementById('mobile-drawer');
        const close = document.getElementById('mobile-menu-close');

        if (btn && drawer && close) {
            btn.onclick = () => drawer.classList.remove('translate-x-full');
            close.onclick = () => drawer.classList.add('translate-x-full');
        }
    }
}

// Render Footer
function renderFooter() {
    const mainFooter = document.getElementById('main-footer');
    if (mainFooter) {
        mainFooter.className = "bg-slate-800 text-white mt-12 relative font-sans";
        mainFooter.innerHTML = `
            <!-- Query / CTA box -->
            <div class="max-w-6xl mx-auto px-4 -translate-y-12">
                <div class="bg-brandNavy text-white rounded-bl-3xl rounded-tr-3xl p-8 shadow-xl flex flex-col md:flex-row justify-between items-center gap-6 border-b-4 border-brandCyan">
                    <div class="text-center md:text-left md:w-3/4">
                        <h3 class="text-2xl font-bold font-poppins mb-2">${siteContent.footer.ctaTitle}</h3>
                        <p class="text-slate-300 text-[15px] leading-relaxed">${siteContent.footer.ctaText}</p>
                    </div>
                    <div class="md:w-1/4 text-center">
                        <a href="contact-us.html" class="inline-flex items-center gap-2 bg-brandGreen hover:bg-brandCyan text-brandNavy font-bold py-3 px-6 rounded-full shadow transition-all duration-300 group">
                            <span>${siteContent.footer.ctaBtnText}</span>
                            <i class="fa-solid fa-angle-right group-hover:translate-x-1 transition-transform"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Footer Main columns -->
            <div class="max-w-7xl mx-auto px-6 pb-12 grid grid-cols-1 md:grid-cols-3 gap-10">
                <!-- Col 1: Bio -->
                <div class="flex flex-col gap-4">
                    <img id="footer-logo-img" class="h-16 w-fit object-contain mb-2" alt="Footer Logo">
                    <p class="text-slate-300 text-[15px] leading-relaxed text-justify">${siteContent.footer.bio}</p>
                </div>

                <!-- Col 2: Quick Links -->
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <h4 class="text-lg font-bold border-b-2 border-brandGreen w-fit pb-1 mb-4 font-poppins">Quick Links</h4>
                        <ul class="flex flex-col gap-2 text-[15px] text-slate-300">
                            ${siteContent.footer.quickLinksCol1.map(link => {
            let url = "index.html";
            if (link === "About Us") url = "about.html";
            else if (link === "Admission") url = "admission-process.html";
            else if (link === "Teaching Staff") url = "teaching-staff.html";
            else if (link === "Non Teaching Staff") url = "non-teaching-staff.html";
            else if (link === "Facilities") url = "facilities.html";
            else if (link === "Courses") url = "b-pharm.html";
            else if (link === "Academic") url = "syllabus.html";
            else if (link === "Gallery") url = "gallery.html";
            else if (link === "News & Events") url = "news-events.html";
            else if (link === "Contact Us") url = "contact-us.html";
            return `<li><a href="${url}" class="hover:text-brandCyan transition-colors">${link}</a></li>`;
        }).join('')}
                        </ul>
                    </div>
                    <div>
                        <h4 class="text-lg font-bold border-b-2 border-brandGreen w-fit pb-1 mb-4 font-poppins">Programs</h4>
                        <ul class="flex flex-col gap-2 text-[15px] text-slate-300">
                            ${siteContent.footer.quickLinksCol2.map(link => {
            let url = "#";
            if (link === "Gallery") url = "gallery.html";
            return `<li><a href="${url}" class="hover:text-brandCyan transition-colors">${link}</a></li>`;
        }).join('')}
                        </ul>
                    </div>
                </div>

                <!-- Col 3: Contact -->
                <div class="flex flex-col gap-4">
                    <h4 class="text-lg font-bold border-b-2 border-brandGreen w-fit pb-1 mb-4 font-poppins">Reach Us At</h4>
                    <ul class="flex flex-col gap-3 text-[15px] text-slate-300">
                        <li class="flex gap-3">
                            <span class="bg-brandGreen text-brandNavy h-9 w-9 flex items-center justify-center rounded-full shrink-0 font-bold"><i class="fa-solid fa-map-marker-alt"></i></span>
                            <span>${siteContent.footer.contactAddress}</span>
                        </li>
                        <li class="flex gap-3">
                            <span class="bg-brandGreen text-brandNavy h-9 w-9 flex items-center justify-center rounded-full shrink-0 font-bold"><i class="fa-solid fa-mobile-alt"></i></span>
                            <span>${siteContent.footer.contactPhone}</span>
                        </li>
                        <li class="flex gap-3">
                            <span class="bg-brandGreen text-brandNavy h-9 w-9 flex items-center justify-center rounded-full shrink-0 font-bold"><i class="fa-solid fa-envelope"></i></span>
                            <span class="break-all">${siteContent.footer.contactEmail}</span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Big number banner -->
            <div class="bg-slate-900 border-t border-slate-700 py-6 text-center text-3xl md:text-5xl font-black font-poppins tracking-wider text-slate-400 bg-opacity-50">
                ${siteContent.footer.contactHugeNumber}
            </div>

            <!-- Bottom Copyright -->
            <div class="bg-brandNavy py-4 px-6 border-t border-slate-700">
                <div class="max-w-7xl mx-auto flex justify-center items-center text-sm text-slate-400">
                    <p class="font-semibold text-center">${siteContent.footer.copyright}</p>
                </div>
            </div>
        `;

        setElementImage('footer-logo-img', siteContent.footer.logoFooter, 'Footer Logo');
    }
}

// ---------------------------------
// PAGE SPECIFIC LOADING BEHAVIORS
// ---------------------------------

function initHomePage() {
    // 1. Slider Setup
    const sliderContainer = document.getElementById('hero-slider');
    if (sliderContainer) {
        sliderContainer.innerHTML = siteContent.home.sliderImages.map((src, idx) => `
            <div class="hero-slide ${idx === 0 ? 'active' : ''}" style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('${resolveImageUrl(src)}');"></div>
        `).join('');

        let currentSlide = 0;
        const slides = sliderContainer.getElementsByClassName('hero-slide');
        if (slides.length > 0) {
            setInterval(() => {
                slides[currentSlide].classList.remove('active');
                currentSlide = (currentSlide + 1) % slides.length;
                slides[currentSlide].classList.add('active');
            }, 5000); // 5 seconds interval
        }
    }

    // 2. Highlights
    const highlightsGrid = document.getElementById('highlights-grid');
    if (highlightsGrid) {
        highlightsGrid.className = "bg-white shadow-2xl rounded-3xl p-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto relative z-30 -translate-y-16 md:-translate-y-24 border border-slate-100";
        highlightsGrid.innerHTML = siteContent.home.highlights.map((h, idx) => `
            <div class="border-l-2 border-[#47ba7d] pl-6 py-2 flex flex-col items-center text-center justify-center gap-3 w-full anim-slideInUp stagger-${idx + 1}">
                <div class="h-16 w-16 rounded-full bg-[#47ba7d] text-white flex items-center justify-center text-2xl shadow-md transform hover:scale-110 transition-transform">
                    <i class="fa-solid ${idx === 0 ? 'fa-lightbulb' : idx === 1 ? 'fa-school' : idx === 2 ? 'fa-building' : 'fa-certificate'}"></i>
                </div>
                <h5 class="text-[17px] font-bold font-poppins text-[#0c2b5c] tracking-wide">${h.title}</h5>
            </div>
        `).join('');
    }

    // 3. Courses Highlight (tabbed, mirrors arunodayaginstitutions.in Courses Offered section)
    const coursesList = siteContent.home.coursesList;
    const coursesHighlight = document.getElementById('courses-highlight');
    if (coursesHighlight && coursesList && coursesList.length) {
        coursesHighlight.className = "anim-slideInUp";

        const renderCoursesPanel = (idx) => {
            const ch = coursesList[idx];
            return `
            <div class="flex flex-col md:flex-row bg-white rounded-bl-[40px] rounded-tr-[40px] border border-slate-200 shadow-lg overflow-hidden max-w-6xl mx-auto min-h-[500px]">
                <!-- Left Column: Courses Image -->
                <div class="md:w-1/2 w-full h-64 sm:h-80 md:h-auto relative overflow-hidden">
                    <img src="${resolveImageUrl(ch.img)}" alt="${ch.name}" class="w-full h-full object-cover object-left">
                </div>
                <!-- Right Column: Courses Content -->
                <div class="md:w-1/2 w-full p-6 md:p-12 flex flex-col justify-center">
                    <span class="text-sm font-bold text-[#47ba7d] uppercase tracking-widest block mb-2">${siteContent.home.coursesTitle}</span>
                    <div class="w-full h-0.5 border-t border-dotted border-slate-300 mb-4"></div>
                    <h2 class="text-2xl md:text-4xl font-bold font-poppins text-[#0c2b5c] mb-4">${ch.name}</h2>
                    <p class="text-slate-600 leading-relaxed text-justify mb-6 text-[15px]">${ch.desc}</p>
                    <div>
                        <a href="${ch.link}" class="inline-flex items-center gap-2 bg-[#47ba7d] hover:bg-[#0c2b5c] text-white font-bold py-2.5 px-6 rounded-full shadow transition-all duration-300 group text-[15px]">
                            <span>Read More</span> <i class="fa-solid fa-angle-right text-[12px] group-hover:translate-x-1 transition-transform"></i>
                        </a>
                    </div>
                </div>
            </div>`;
        };

        const renderTabs = (activeIdx) => coursesList.map((c, idx) => `
            <button type="button" data-course-tab="${idx}" class="course-tab-btn px-5 py-2.5 rounded-full text-sm font-bold font-poppins tracking-wide transition-all duration-300 border ${idx === activeIdx ? 'bg-brandNavy text-white border-brandNavy shadow' : 'bg-white text-brandNavy border-slate-200 hover:border-brandCyan hover:text-brandCyan'}">${c.tab}</button>
        `).join('');

        const renderAll = (activeIdx) => {
            coursesHighlight.innerHTML = `
                <div class="flex flex-wrap justify-center gap-3 mb-6" id="courses-tab-bar">
                    ${renderTabs(activeIdx)}
                </div>
                <div id="courses-tab-panel">${renderCoursesPanel(activeIdx)}</div>
            `;

            coursesHighlight.querySelectorAll('.course-tab-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const idx = parseInt(btn.getAttribute('data-course-tab'), 10);
                    renderAll(idx);
                });
            });
        };

        renderAll(0);
    }

    // 4. Facilities
    const facilitiesGrid = document.getElementById('facilities-grid');
    if (facilitiesGrid) {
        facilitiesGrid.innerHTML = siteContent.home.facilities.map((f, idx) => `
            <div class="bg-white rounded-bl-2xl rounded-tr-2xl p-6 border border-slate-200 shadow-sm hover:shadow-md transition-shadow anim-slideInUp stagger-${idx + 1}">
                <div class="flex items-center gap-3 mb-3">
                    <span class="h-10 w-10 flex items-center justify-center rounded-full bg-brandCyan bg-opacity-20 text-brandCyan text-lg font-bold"><i class="fa-solid ${idx === 0 ? 'fa-book' : idx === 1 ? 'fa-bus' : idx === 2 ? 'fa-volleyball' : 'fa-compass'}"></i></span>
                    <h4 class="text-lg font-bold text-brandNavy font-poppins">${f.name}</h4>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">${f.desc}</p>
            </div>
        `).join('');
    }

    // 5. Welcome section
    const welcomeSection = document.getElementById('welcome-section');
    if (welcomeSection) {
        const welcome = siteContent.home.welcome;
        welcomeSection.className = "welcome-bg text-white rounded-bl-[40px] rounded-tr-[40px] shadow-xl overflow-hidden max-w-6xl mx-auto flex flex-col md:flex-row min-h-[500px] anim-slideInUp";
        welcomeSection.innerHTML = `
            <!-- Left Column: Welcome Image -->
            <div class="md:w-1/2 w-full min-h-[350px] md:min-h-full anim-slideInLeft relative overflow-hidden" style="background-image: url('${resolveImageUrl(welcome.img || 'Images/Home/about collage.png')}'); background-size: cover; background-position: center top; border-radius: 0px 0px 0px 25px;">
            </div>
            <!-- Right Column: Welcome Text -->
            <div class="md:w-1/2 w-full p-8 md:p-12 flex flex-col justify-center anim-slideInRight">
                <span class="text-sm font-bold text-brandCyan uppercase tracking-widest block mb-2">Welcome</span>
                <h2 class="text-3xl md:text-4xl font-extrabold font-poppins mb-4">${welcome.title}</h2>
                <div class="w-16 h-1 bg-brandGreen mb-6"></div>
                <div class="text-[15px] leading-relaxed flex flex-col gap-4 text-slate-100 text-justify">
                    <p>${welcome.p1}</p>
                    <p>${welcome.p2}</p>
                </div>
                <div class="mt-8">
                    <a href="about.html" class="inline-flex items-center gap-2 bg-brandGreen hover:bg-brandCyan text-brandNavy font-bold py-3 px-8 rounded-full shadow transition-all duration-300 group">
                        <span>${welcome.linkText}</span> <i class="fa-solid fa-angle-right group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </div>
        `;
    }

    // 6. Placements
    const placementsTitle = document.getElementById('placements-title');
    if (placementsTitle) {
        placementsTitle.innerText = siteContent.home.placementsTitle;
        placementsTitle.className = "text-3xl md:text-4xl font-extrabold text-brandNavy font-poppins text-center mb-10 tracking-tight anim-slideInUp";
    }

    const placementsGrid = document.getElementById('placements-grid');
    if (placementsGrid) {
        // Change grid to a marquee overflow wrapper
        placementsGrid.className = "relative overflow-hidden w-full py-4 anim-slideInUp stagger-2";

        // Duplicate placement logos for infinite loop
        const doublePlacements = [...siteContent.home.placements, ...siteContent.home.placements];

        placementsGrid.innerHTML = `
            <div class="logo-marquee-track flex gap-8 items-center w-max">
                ${doublePlacements.map((src, idx) => `
                    <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm flex items-center justify-center hover:shadow-md transition-shadow h-24 w-40 shrink-0">
                        <img id="placement-logo-${idx}" class="max-h-full max-w-full object-contain" alt="Placement Logo">
                    </div>
                `).join('')}
            </div>
        `;

        doublePlacements.forEach((src, idx) => {
            setElementImage(`placement-logo-${idx}`, src, `Placement logo ${idx + 1}`);
        });
    }

    // 7. Members
    const membersTitle = document.getElementById('members-title');
    if (membersTitle) {
        membersTitle.innerText = siteContent.home.membersTitle;
        membersTitle.className = "text-3xl md:text-4xl font-extrabold text-brandNavy font-poppins text-center mb-10 tracking-tight anim-slideInUp";
    }

    const membersGrid = document.getElementById('members-grid');
    if (membersGrid) {
        membersGrid.innerHTML = siteContent.home.members.map((m, idx) => `
            <div class="bg-white border border-slate-200 rounded-bl-3xl rounded-tr-3xl overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col anim-slideInUp stagger-${idx + 1}">
                <div class="h-64 bg-slate-100 relative overflow-hidden group">
                    <img id="member-photo-${idx}" class="w-full h-full object-cover object-top transform group-hover:scale-110 transition-transform duration-500" alt="${m.name}">
                </div>
                <div class="p-6 text-center border-t border-slate-100 flex-grow">
                    <h5 class="text-lg font-bold text-brandNavy font-poppins">${m.name}</h5>
                    <p class="text-brandCyan text-sm font-semibold mb-1">${m.role}</p>
                    <p class="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-3">${m.role2}</p>
                    <a href="tel:${m.phone}" class="inline-flex items-center gap-1 text-slate-700 hover:text-brandCyan font-bold text-sm bg-slate-100 py-1.5 px-4 rounded-full transition-colors">
                        <i class="fa-solid fa-phone text-xs"></i> ${m.phone}
                    </a>
                </div>
            </div>
        `).join('');

        siteContent.home.members.forEach((m, idx) => {
            setElementImage(`member-photo-${idx}`, m.img, m.name);
        });
    }

    // 8. Vision & Mission
    const visionBox = document.getElementById('vision-box');
    if (visionBox) {
        const v = siteContent.home.vision;
        visionBox.className = "anim-slideInLeft";
        visionBox.innerHTML = `
            <div class="bg-brandNavy text-white rounded-bl-3xl rounded-tr-3xl p-8 border-b-4 border-brandCyan h-full shadow-md">
                <div class="flex items-center gap-3 mb-4">
                    <span class="text-3xl text-brandGreen"><i class="fa-solid fa-eye"></i></span>
                    <h2 class="text-2xl font-bold font-poppins">${v.title}</h2>
                </div>
                <p class="text-slate-300 leading-relaxed text-justify text-[15px]">${v.text}</p>
            </div>
        `;
    }

    const missionBox = document.getElementById('mission-box');
    if (missionBox) {
        const m = siteContent.home.mission;
        missionBox.className = "anim-slideInRight";
        missionBox.innerHTML = `
            <div class="bg-white text-slate-800 rounded-bl-3xl rounded-tr-3xl p-8 border border-slate-200 border-b-4 border-brandGreen h-full shadow-md">
                <div class="flex items-center gap-3 mb-4">
                    <span class="text-3xl text-brandCyan"><i class="fa-solid fa-rocket"></i></span>
                    <h2 class="text-2xl font-bold font-poppins text-brandNavy">${m.title}</h2>
                </div>
                <p class="text-slate-600 leading-relaxed text-justify text-[15px]">${m.text}</p>
            </div>
        `;
    }

    // 9. Why Us
    const whyUsTitle = document.getElementById('why-us-title');
    if (whyUsTitle) {
        whyUsTitle.innerText = siteContent.home.whyUsTitle;
        whyUsTitle.className = "text-3xl md:text-4xl font-extrabold font-poppins text-center mb-10 tracking-tight text-brandGreen anim-slideInUp";
    }

    const whyUsList = document.getElementById('why-us-list');
    if (whyUsList) {
        whyUsList.className = "grid grid-cols-1 md:grid-cols-2 gap-4 max-w-5xl mx-auto px-6";
        whyUsList.innerHTML = siteContent.home.whyUs.map((w, idx) => `
            <div class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm anim-slideInUp stagger-${(idx % 5) + 1}">
                <span class="h-6 w-6 rounded-full bg-brandGreen text-white flex items-center justify-center shrink-0 text-sm font-bold"><i class="fa-solid fa-check"></i></span>
                <span class="text-brandNavy font-semibold text-[15px]">${w}</span>
            </div>
        `).join('');
    }

    // 10. Stats counter animation
    const statsContainer = document.getElementById('stats-container');
    if (statsContainer) {
        statsContainer.className = "max-w-5xl mx-auto flex flex-wrap justify-center items-center gap-6 anim-slideInUp";
        statsContainer.innerHTML = siteContent.home.stats.map((s, idx) => `
            <div class="text-center bg-slate-100 p-6 rounded-2xl border border-slate-200 shadow-sm shrink-0 w-48 mx-auto md:w-56">
                <div class="text-4xl font-extrabold text-brandBlue font-poppins mb-1">
                    <span class="stat-number" data-target="${s.value}">0</span>+
                </div>
                <div class="text-sm font-bold text-slate-500 uppercase tracking-widest">${s.label}</div>
            </div>
        `).join('');

        // IntersectionObserver for Counter
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counters = statsContainer.querySelectorAll('.stat-number');
                    counters.forEach(c => {
                        const target = parseInt(c.getAttribute('data-target'));
                        let count = 0;
                        const speed = Math.max(10, Math.floor(2000 / target)); // duration 2 seconds approx
                        const timer = setInterval(() => {
                            count += Math.ceil(target / 40);
                            if (count >= target) {
                                c.innerText = target;
                                clearInterval(timer);
                            } else {
                                c.innerText = count;
                            }
                        }, speed);
                    });
                    observer.unobserve(statsContainer);
                }
            });
        }, { threshold: 0.2 });
        observer.observe(statsContainer);
    }

    // 11. Announcements Infinite Scrolling
    const annTitle = document.getElementById('announcements-title');
    if (annTitle) annTitle.innerText = siteContent.home.announcementsTitle;

    const annTicker = document.getElementById('announcements-ticker-items');
    if (annTicker) {
        // Duplicate items list to create seamless infinite scrolling marquee loop
        const items = [...siteContent.home.announcements, ...siteContent.home.announcements];
        annTicker.innerHTML = items.map((ann, idx) => `
            <div class="p-4 bg-slate-50 hover:bg-slate-100 rounded-xl border border-slate-200 border-l-4 border-brandCyan mb-3 shadow-sm hover:shadow transition-all cursor-pointer">
                <div class="flex items-start gap-2.5">
                    <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-bullhorn animate-pulse"></i></span>
                    <p class="text-brandNavy text-sm font-bold leading-normal">${ann}</p>
                </div>
            </div>
        `).join('');
    }

    // 12. Home Quick Links
    const qLinksTitle = document.getElementById('home-quick-links-title');
    if (qLinksTitle) qLinksTitle.innerText = siteContent.home.quickLinksTitle;

    const qLinksList = document.getElementById('home-quick-links');
    if (qLinksList) {
        qLinksList.innerHTML = siteContent.home.quickLinks.map(q => `
            <a href="${q.link}" class="flex items-center justify-between bg-brandBlue hover:bg-brandCyan text-white font-bold py-4 px-6 rounded-xl shadow transition-all duration-300 group">
                <span>${q.text}</span>
                <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
            </a>
        `).join('');
    }

    // 13. Pop-up slider modal
    const modal = document.getElementById('myModal');
    if (modal) {
        // Injects photos inside slideBox
        const slideBox = document.getElementById('slideBox');
        if (slideBox) {
            slideBox.innerHTML = siteContent.home.modalSliderImages.map((src, idx) => `
                <img id="modal-slide-${idx}" class="w-full shrink-0 object-cover object-center h-80 md:h-[450px]" alt="Modal slide ${idx + 1}">
            `).join('');

            siteContent.home.modalSliderImages.forEach((src, idx) => {
                setElementImage(`modal-slide-${idx}`, src, `Modal slide ${idx + 1}`);
            });
        }

        // Show modal on load
        modal.style.display = 'block';

        const closeBtn = modal.querySelector('.close');
        if (closeBtn) {
            closeBtn.onclick = () => modal.style.display = 'none';
        }
        window.onclick = (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        };

        // Slider logic inside modal
        let modalIndex = 0;
        const slides = slideBox.children;
        const totalSlides = slides.length;

        window.plusSlides = function (n) {
            if (totalSlides === 0) return;
            modalIndex = (modalIndex + n + totalSlides) % totalSlides;

            // Temporary disable keyframe animation and shift translate x
            slideBox.style.animation = 'none';
            slideBox.style.transform = `translateX(-${modalIndex * 100}%)`;
        };
    }
}

function initAboutPage() {
    const welcome = siteContent.about;

    // Page Title
    const pageTitle = document.getElementById('about-title');
    if (pageTitle) pageTitle.innerText = welcome.title;

    // Welcome Section - 2 columns (Left: way.png image, Right: Text messages)
    const wTitle = document.getElementById('about-welcome-title');
    if (wTitle) {
        const welcomeSection = wTitle.parentElement;
        if (welcomeSection) {
            welcomeSection.className = "max-w-6xl mx-auto px-6 py-16 flex flex-col md:flex-row gap-10 items-center";
            welcomeSection.innerHTML = `
                <!-- Left: way.png image -->
                <div class="md:w-1/2 w-full min-h-[350px] md:min-h-[450px] self-stretch anim-slideInLeft relative overflow-hidden" style="background-image: url('${resolveImageUrl(welcome.welcomeImg || 'Images/Home/way.png')}'); background-size: cover; background-position: center; border-radius: 0px 0px 50px 0px;">
                </div>
                <!-- Right: Welcome Text -->
                <div class="md:w-1/2 w-full anim-slideInRight">
                    <h2 class="text-2xl md:text-3xl font-extrabold font-poppins text-brandNavy mb-6">${welcome.welcomeTitle}</h2>
                    <div class="flex flex-col gap-6 text-[15px] leading-relaxed text-slate-600 text-justify">
                        <p class="font-bold text-brandNavy text-lg">${welcome.welcomeText1}</p>
                        <p>${welcome.welcomeText2}</p>
                        <p>${welcome.welcomeText3}</p>
                    </div>
                </div>
            `;
        }
    }

    // Principal message
    const pTitle = document.getElementById('about-principal-title');
    if (pTitle) {
        pTitle.innerText = welcome.principalTitle;
        // Find main row container of Principal message to set scroll animation
        const pContainer = pTitle.closest('.flex');
        if (pContainer) pContainer.className = "flex flex-col md:flex-row gap-10 items-start anim-slideInUp";
    }
    const pName = document.getElementById('about-principal-name');
    if (pName) pName.innerText = welcome.principalName;
    const pRole = document.getElementById('about-principal-role');
    if (pRole) pRole.innerText = welcome.principalRole;
    const pText = document.getElementById('about-principal-text');
    if (pText) pText.innerText = welcome.principalText;
    setElementImage('about-principal-img', welcome.principalImg, welcome.principalName);

    // Director Message
    const dTitle = document.getElementById('about-director-title');
    if (dTitle) {
        dTitle.innerText = welcome.directorTitle;
        // Find main row container of Director message to set scroll animation
        const dContainer = dTitle.closest('.flex');
        if (dContainer) dContainer.className = "flex flex-col md:flex-row gap-10 items-start anim-slideInUp stagger-2";
    }
    const dName = document.getElementById('about-director-name');
    if (dName) dName.innerText = welcome.directorName;
    const dRole = document.getElementById('about-director-role');
    if (dRole) dRole.innerText = welcome.directorRole + " / " + welcome.directorRole2;
    const dText = document.getElementById('about-director-text');
    if (dText) dText.innerText = welcome.directorText;
    setElementImage('about-director-img', welcome.directorImg, welcome.directorName);

    // Vision / Mission Section containers
    const vText = document.getElementById('about-vision-text');
    if (vText) {
        vText.innerText = welcome.vision;
        const vBox = vText.closest('div');
        if (vBox) vBox.className = "bg-brandNavy text-white rounded-bl-3xl rounded-tr-3xl p-8 border-b-4 border-brandCyan shadow-md anim-slideInLeft";
    }
    const mText = document.getElementById('about-mission-text');
    if (mText) {
        mText.innerText = welcome.mission;
        const mBox = mText.closest('div');
        if (mBox) mBox.className = "bg-white text-slate-800 rounded-bl-3xl rounded-tr-3xl p-8 border border-slate-200 border-b-4 border-brandGreen shadow-md anim-slideInRight";
    }

    // Faculty Grid list
    const facTitle = document.getElementById('about-faculty-title');
    if (facTitle) {
        facTitle.innerText = welcome.facultyTitle;
        facTitle.className = "text-2xl md:text-3xl font-extrabold font-poppins text-brandNavy text-center mb-10 tracking-tight anim-slideInUp";
    }
    const facGrid = document.getElementById('about-faculty-grid');
    if (facGrid) {
        facGrid.innerHTML = welcome.faculties.map((f, idx) => `
            <div class="bg-white border border-slate-200 rounded-2xl p-6 text-center shadow-sm anim-slideInUp stagger-${idx + 1}">
                <div class="h-44 w-44 rounded-full bg-slate-100 mx-auto overflow-hidden border border-slate-200 mb-4 group">
                    <img id="fac-img-${idx}" class="w-full h-full object-cover object-top transform group-hover:scale-110 transition-transform duration-500" alt="${f.name}">
                </div>
                <h5 class="text-[17px] font-bold text-brandNavy font-poppins mb-1">${f.name}</h5>
                <p class="text-brandCyan text-sm font-semibold">${f.role}</p>
                <p class="text-slate-500 text-xs font-semibold uppercase tracking-wider mt-1">${f.qualification}</p>
            </div>
        `).join('');

        welcome.faculties.forEach((f, idx) => {
            setElementImage(`fac-img-${idx}`, f.img, f.name);
        });
    }
}

function initAdmissionPage() {
    const pageTitle = document.getElementById('admission-title');
    if (pageTitle) pageTitle.innerText = siteContent.admission.title;

    const subTitle = document.getElementById('admission-subtitle');
    if (subTitle) {
        const welcomeSection = subTitle.parentElement;
        if (welcomeSection) {
            welcomeSection.className = "max-w-6xl mx-auto px-6 py-12";
            welcomeSection.innerHTML = `
                <h2 class="text-2xl md:text-3xl font-extrabold font-poppins text-brandNavy mb-10 text-center">${siteContent.admission.subtitle}</h2>
                <div class="flex flex-col md:flex-row gap-10 items-center">
                    <!-- Left: Admission Image -->
                    <div class="md:w-1/2 w-full min-h-[300px] md:min-h-[400px] self-stretch anim-slideInLeft relative overflow-hidden" style="background-image: url('${resolveImageUrl(siteContent.admission.img || 'Images/Admission/addmision.png')}'); background-size: cover; background-position: center; border-radius: 20px;">
                    </div>
                    <!-- Right: Requirements List -->
                    <div class="md:w-1/2 w-full anim-slideInRight">
                        <ul class="flex flex-col gap-4">
                            ${siteContent.admission.requirements.map((req, idx) => `
                                <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm anim-slideInUp stagger-${(idx % 6) + 1}">
                                    <span class="h-6 w-6 rounded-full bg-brandCyan text-brandNavy flex items-center justify-center shrink-0 text-sm font-bold"><i class="fa-solid fa-angle-right"></i></span>
                                    <span class="text-brandNavy font-semibold text-[15px]">${req}</span>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>
            `;
        }
    }
}

function initTeachingStaffPage() {
    const pageTitle = document.getElementById('teaching-staff-title');
    if (pageTitle) pageTitle.innerText = siteContent.teachingStaff.title;

    const wrapper = document.getElementById('teaching-staff-wrapper');
    if (wrapper) {
        wrapper.innerHTML = siteContent.teachingStaff.departments.map((dept, deptIdx) => {
            const isBscBcomBca = dept.name.includes("B.Sc / B.Com / BCA");
            return `
                <div class="mb-10 anim-slideInUp stagger-${(deptIdx % 3) + 1}">
                    <h2 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-4">${dept.name}</h2>
                    <div class="overflow-x-auto bg-white rounded-xl shadow-md border border-slate-200">
                        <table class="w-full text-left text-brandNavy">
                            <thead>
                                <tr class="bg-brandBlue text-white font-poppins text-[15px] border-b border-slate-200">
                                    <th class="p-4 w-20 text-center font-semibold">SL. No</th>
                                    <th class="p-4 font-semibold">Name of the Staff</th>
                                    <th class="p-4 font-semibold">Qualification</th>
                                    <th class="p-4 font-semibold">${isBscBcomBca ? 'Subject' : 'Designation'}</th>
                                    <th class="p-4 w-32 text-center font-semibold">Photo</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${dept.staff.map((s, idx) => `
                                    <tr class="border-b border-slate-200 last:border-0 hover:bg-slate-50 transition-colors">
                                        <td class="p-4 text-center font-bold text-slate-500">${s.no}</td>
                                        <td class="p-4 font-bold text-[15px]">${s.name}</td>
                                        <td class="p-4 text-slate-600 font-semibold text-[14px]">${s.qualification}</td>
                                        <td class="p-4 text-slate-700 font-bold text-[14px]">${isBscBcomBca ? s.designation : s.designation}</td>
                                        <td class="p-3 text-center">
                                            ${s.photo ? `
                                                <img src="${resolveImageUrl(s.photo)}" class="h-16 w-16 object-cover rounded-full mx-auto border border-slate-200" alt="${s.name}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                                                <div class="h-16 w-16 bg-slate-100 border border-slate-200 rounded-full mx-auto overflow-hidden flex items-center justify-center text-slate-400 text-xl" style="display:none;">
                                                    <i class="fa-regular fa-user"></i>
                                                </div>
                                            ` : `
                                                <div class="h-16 w-16 bg-slate-100 border border-slate-200 rounded-full mx-auto overflow-hidden flex items-center justify-center text-slate-400 text-xl">
                                                    <i class="fa-regular fa-user"></i>
                                                </div>
                                            `}
                                        </td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }).join('');
    }
}

function initNonTeachingStaffPage() {
    const pageTitle = document.getElementById('non-teaching-staff-title');
    if (pageTitle) pageTitle.innerText = siteContent.nonTeachingStaff.title;

    const tableBody = document.getElementById('non-teaching-staff-tbody');
    if (tableBody) {
        tableBody.innerHTML = siteContent.nonTeachingStaff.staff.map(s => `
            <tr class="border-b border-slate-200 last:border-0 hover:bg-slate-50 transition-colors">
                <td class="p-4 text-center font-bold text-slate-500">${s.no}</td>
                <td class="p-4 font-bold text-[15px]">${s.name}</td>
                <td class="p-4 text-slate-600 font-semibold text-[14px]">${s.qualification}</td>
                <td class="p-4 text-slate-700 font-bold text-[14px]">${s.designation}</td>
                <td class="p-3 text-center">
                    ${s.photo ? `
                        <img src="${resolveImageUrl(s.photo)}" class="h-16 w-16 object-cover rounded-full mx-auto border border-slate-200" alt="${s.name}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                        <div class="h-16 w-16 bg-slate-100 border border-slate-200 rounded-full mx-auto overflow-hidden flex items-center justify-center text-slate-400 text-xl" style="display:none;">
                            <i class="fa-regular fa-user"></i>
                        </div>
                    ` : `
                        <div class="h-16 w-16 bg-slate-100 border border-slate-200 rounded-full mx-auto overflow-hidden flex items-center justify-center text-slate-400 text-xl">
                            <i class="fa-regular fa-user"></i>
                        </div>
                    `}
                </td>
            </tr>
        `).join('');
    }
}

function initFacilitiesPage() {
    const pageTitle = document.getElementById('facilities-title');
    if (pageTitle) pageTitle.innerText = siteContent.facilitiesPage.title;

    const grid = document.getElementById('facilities-grid');
    if (grid) {
        grid.innerHTML = siteContent.facilitiesPage.facilities.map((f, idx) => `
            <div class="bg-white rounded-bl-3xl rounded-tr-3xl p-8 border border-slate-200 shadow-sm hover:shadow-md transition-shadow anim-slideInUp stagger-${(idx % 4) + 1}">
                <div class="flex items-center gap-4 mb-4">
                    <span class="h-12 w-12 flex items-center justify-center rounded-full bg-brandCyan bg-opacity-20 text-brandCyan text-2xl font-bold"><i class="fa-solid ${idx === 0 ? 'fa-book' : idx === 1 ? 'fa-bed' : idx === 2 ? 'fa-bus' : idx === 3 ? 'fa-volleyball' : idx === 4 ? 'fa-utensils' : 'fa-compass'}"></i></span>
                    <h4 class="text-xl font-bold text-brandNavy font-poppins">${f.name}</h4>
                </div>
                <p class="text-slate-600 leading-relaxed text-justify text-[15px]">${f.desc}</p>
            </div>
        `).join('');
    }
}

function initCoursePage(courseKey) {
    const c = siteContent.courses[courseKey];
    if (!c) return;

    // Set page title
    document.title = c.title + " - Arunodaya Institutions";

    // Render the page title banner (matches the navy title banner used on every other inner page)
    const titleBanner = document.getElementById('course-title-banner');
    if (titleBanner) titleBanner.innerText = c.title;

    // Render the "Courses Offered" highlight card (mirrors the card used on the
    // homepage and on each individual course page of the live site)
    const offeredCard = document.getElementById('course-offered-card');
    if (offeredCard) {
        offeredCard.className = "anim-slideInUp";
        offeredCard.innerHTML = `
            <div class="flex flex-col md:flex-row bg-white rounded-bl-[40px] rounded-tr-[40px] border border-slate-200 shadow-lg overflow-hidden max-w-6xl mx-auto min-h-[420px]">
                <div class="md:w-1/2 w-full min-h-[300px] md:min-h-full anim-slideInLeft relative overflow-hidden" style="background-image: url('${resolveImageUrl(c.heroImg)}'); background-size: cover; background-position: center top; border-radius: 0px 0px 0px 25px;">
                </div>
                <div class="md:w-1/2 w-full p-8 md:p-12 flex flex-col justify-center anim-slideInRight">
                    <span class="text-sm font-bold text-brandGreen uppercase tracking-widest block mb-2">${siteContent.home.coursesTitle}</span>
                    <div class="w-24 h-0.5 border-t border-dotted border-slate-300 mb-4"></div>
                    <h2 class="text-3xl font-bold font-poppins text-brandNavy mb-4">${c.name}</h2>
                    <p class="text-slate-600 leading-relaxed text-justify text-[15px]">${c.description}</p>
                </div>
            </div>
        `;
    }
    const nameEl = document.getElementById('course-name');
    if (nameEl) nameEl.innerText = c.name;

    // Optional languages grid
    const langSection = document.getElementById('languages-section');
    if (langSection && c.languages) {
        langSection.innerHTML = `
            <h4 class="text-lg font-bold text-brandNavy mb-3 font-poppins">${c.part1Title}</h4>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-3">
                ${c.languages.map(l => `<div class="bg-white border border-slate-200 p-3 rounded-lg text-center font-bold text-brandNavy shadow-sm">${l}</div>`).join('')}
            </div>
            <p class="text-sm font-bold text-slate-500">${c.forUgText}</p>
        `;
    }

    // Optional list (Scope or Part II options)
    const scopeTitle = document.getElementById('scope-title');
    const scopeDesc = document.getElementById('scope-desc');
    const scopeList = document.getElementById('scope-list');
    const scopeItems = c.scopeOpportunities || c.combinations;
    const hasScope = !!(c.scopeTitle || c.part2Title || c.scopeDesc || (scopeItems && scopeItems.length));
    // Hide the entire scope grid wrapper if this course has no scope-style data
    const scopeWrapper = scopeTitle ? scopeTitle.closest('.grid') : null;
    if (scopeWrapper) scopeWrapper.style.display = hasScope ? 'grid' : 'none';
    if (hasScope) {
        if (scopeTitle) scopeTitle.innerText = c.scopeTitle || c.part2Title || '';
        if (scopeDesc) {
            if (c.scopeDesc) {
                scopeDesc.innerText = c.scopeDesc;
                scopeDesc.style.display = 'block';
            } else {
                scopeDesc.style.display = 'none';
            }
        }
        if (scopeList) {
            if (scopeItems && scopeItems.length) {
                scopeList.innerHTML = scopeItems.map(item => `
                    <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm font-semibold text-brandNavy">
                        <span class="h-6 w-6 rounded-full bg-brandCyan text-brandNavy flex items-center justify-center shrink-0 text-xs"><i class="fa-solid fa-check"></i></span>
                        <span>${item}</span>
                    </li>
                `).join('');
                if (scopeList.parentElement) scopeList.parentElement.style.display = 'block';
            } else {
                if (scopeList.parentElement) scopeList.parentElement.style.display = 'none';
            }
        }
    }

    // Approvals Section
    const approvalSection = document.getElementById('approval-section');
    if (approvalSection) {
        if (c.approvalTitle && c.approvals) {
            approvalSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.approvalTitle}</h3>
                <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${c.approvals.map(app => `
                        <li class="flex items-start gap-3 bg-slate-50 border border-slate-200 p-4 rounded-xl shadow-sm font-semibold text-slate-700">
                            <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-stamp"></i></span>
                            <span>${app}</span>
                        </li>
                    `).join('')}
                </ul>
            `;
            approvalSection.style.display = 'block';
        } else {
            approvalSection.style.display = 'none';
        }
    }

    // Jobs Section
    const jobTitle = document.getElementById('job-title');
    const jobList = document.getElementById('job-list');
    // The visible slate-50 bar is the grandparent (the outer styled wrapper)
    const jobsWrapper = jobTitle ? jobTitle.parentElement.parentElement : null;
    if (c.jobTitle && c.jobs && c.jobs.length) {
        if (jobTitle) jobTitle.innerText = c.jobTitle;
        if (jobList) {
            jobList.innerHTML = c.jobs.map(job => `
                <div class="bg-brandNavy text-white p-4 rounded-xl text-center font-bold tracking-wide shadow-sm hover:bg-brandCyan hover:text-brandNavy transition-colors">${job}</div>
            `).join('');
        }
        if (jobsWrapper) jobsWrapper.style.display = 'block';
    } else {
        if (jobsWrapper) jobsWrapper.style.display = 'none';
    }

    // Subjects List for BCA
    const subjectsSection = document.getElementById('subjects-section');
    if (subjectsSection) {
        if (c.subjects) {
            subjectsSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.semTitle}</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    ${c.subjects.map(sub => `
                        <div class="bg-white border border-slate-200 p-4 rounded-xl shadow-sm font-bold text-brandNavy flex items-center gap-3">
                            <span class="h-8 w-8 rounded-full bg-slate-100 flex items-center justify-center text-brandCyan text-sm font-bold"><i class="fa-solid fa-book-open"></i></span>
                            <span>${sub}</span>
                        </div>
                    `).join('')}
                </div>
            `;
            subjectsSection.style.display = 'block';
        } else {
            subjectsSection.style.display = 'none';
        }
    }

    // Claim of Exemptions for BCA
    const exemptionSection = document.getElementById('exemption-section');
    if (exemptionSection) {
        if (c.exemptionTitle && c.exemptionPoints) {
            exemptionSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.exemptionTitle}</h3>
                <ul class="flex flex-col gap-4">
                    ${c.exemptionPoints.map(ex => `
                        <li class="flex items-start gap-3 bg-slate-50 border border-slate-200 p-4 rounded-xl shadow-sm font-semibold text-slate-700">
                            <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-circle-exclamation"></i></span>
                            <span>${ex}</span>
                        </li>
                    `).join('')}
                </ul>
            `;
            exemptionSection.style.display = 'block';
        } else {
            exemptionSection.style.display = 'none';
        }
    }

    // Eligibility
    const eligTitle = document.getElementById('eligibility-title');
    const eligDesc = document.getElementById('eligibility-desc');
    const eligList = document.getElementById('eligibility-list');
    const eligPoints = c.eligibilityPoints || c.semEligibility;
    const hasElig = !!(c.eligibilityTitle || c.eligibilityDesc || (eligPoints && eligPoints.length));
    if (hasElig) {
        if (eligTitle) eligTitle.innerText = c.eligibilityTitle || '';
        if (eligDesc) {
            if (c.eligibilityDesc) {
                eligDesc.innerText = c.eligibilityDesc;
                eligDesc.style.display = 'block';
            } else {
                eligDesc.style.display = 'none';
            }
        }
        if (eligList && eligPoints && eligPoints.length) {
            eligList.innerHTML = eligPoints.map(pt => `
                <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm font-semibold text-slate-700">
                    <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-user-check"></i></span>
                    <span>${pt}</span>
                </li>
            `).join('');
        }
    }
    // Hide the eligibility column if empty
    if (eligTitle && eligTitle.parentElement) {
        eligTitle.parentElement.style.display = hasElig ? 'block' : 'none';
    }

    // Duration
    const durTitle = document.getElementById('duration-title');
    const durDesc = document.getElementById('duration-desc');
    const durList = document.getElementById('duration-list');
    const hasDur = !!(c.durationTitle || c.studyTitle || c.durationDesc || (c.studyPoints && c.studyPoints.length));
    if (hasDur) {
        if (durTitle) durTitle.innerText = c.durationTitle || c.studyTitle || '';
        if (durDesc) {
            if (c.durationDesc) {
                durDesc.innerText = c.durationDesc;
                durDesc.style.display = 'block';
            } else {
                durDesc.style.display = 'none';
            }
        }
        if (durList) {
            if (c.studyPoints && c.studyPoints.length) {
                durList.innerHTML = c.studyPoints.map(pt => `
                    <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm font-semibold text-slate-700">
                        <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-clock"></i></span>
                        <span>${pt}</span>
                    </li>
                `).join('');
                durList.style.display = 'flex';
            } else {
                durList.style.display = 'none';
            }
        }
    }
    // Hide the duration column if empty
    if (durTitle && durTitle.parentElement) {
        durTitle.parentElement.style.display = hasDur ? 'block' : 'none';
    }
    // Hide the whole eligibility/duration grid if both halves are empty
    if (eligTitle) {
        const eligGrid = eligTitle.closest('.grid');
        if (eligGrid) eligGrid.style.display = (hasElig || hasDur) ? 'grid' : 'none';
    }

    // Required Docs for Degrees
    const docsSection = document.getElementById('docs-section');
    if (docsSection) {
        if (c.docsTitle && c.docs) {
            docsSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.docsTitle}</h3>
                <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${c.docs.map(doc => `
                        <li class="flex items-start gap-3 bg-white border border-slate-200 p-4 rounded-xl shadow-sm font-semibold text-slate-700">
                            <span class="text-brandGreen text-lg shrink-0 mt-0.5"><i class="fa-solid fa-file-invoice"></i></span>
                            <span>${doc}</span>
                        </li>
                    `).join('')}
                </ul>
            `;
            docsSection.style.display = 'block';
        } else {
            docsSection.style.display = 'none';
        }
    }

    const courseFooter = document.getElementById('course-footer-text');
    if (courseFooter) {
        if (c.footerText) {
            courseFooter.innerText = c.footerText;
            courseFooter.style.display = 'block';
        } else {
            courseFooter.style.display = 'none';
        }
    }
}

function initTablePage(pageKey) {
    const data = siteContent[pageKey];
    if (!data) return;

    // Header Title
    const titleEl = document.getElementById('table-page-title');
    if (titleEl) titleEl.innerText = data.title;

    // Headers
    const headersTr = document.getElementById('table-headers');
    if (headersTr) {
        headersTr.innerHTML = data.headers.map(h => `<th class="p-4 font-bold text-[15px]">${h}</th>`).join('');
    }

    // Rows
    const tbody = document.getElementById('table-body');
    if (tbody) {
        tbody.innerHTML = data.rows.map(row => `
            <tr class="border-b border-slate-200 last:border-0 hover:bg-slate-50 transition-colors">
                <td class="p-4 text-center font-bold text-slate-500">${row.no}</td>
                <td class="p-4 font-bold">${row.courseName}</td>
                <td class="p-4 font-semibold text-slate-700">${row.year}</td>
                <td class="p-4">
                    <a href="${resolveImageUrl(row.link)}" target="_blank" class="inline-flex items-center gap-1.5 text-brandCyan hover:text-brandNavy font-bold">
                        <i class="fa-solid fa-file-pdf text-red-500"></i> ${row.attachmentText}
                    </a>
                </td>
            </tr>
        `).join('');
    }
}

function initGalleryPage() {
    const pageTitle = document.getElementById('gallery-title');
    if (pageTitle) pageTitle.innerText = siteContent.gallery.title;

    const grid = document.getElementById('gallery-grid');
    if (grid) {
        grid.innerHTML = siteContent.gallery.images.map((img, idx) => `
            
                <img id="gallery-img-${idx}" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300" alt="${img.title}"<div class="group relative bg-slate-100 rounded-2xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-md cursor-pointer aspect-video">
                <div class="absolute inset-0 bg-black bg-opacity-40 flex items-end p-4 opacity-0 group-hover:opacity-100 transition-opacity">
                    <h5 class="text-white font-bold font-poppins text-sm truncate w-full">${img.title}</h5>
                </div>
            </div>
        `).join('');

        siteContent.gallery.images.forEach((img, idx) => {
            setElementImage(`gallery-img-${idx}`, img.src, img.title);
        });
    }

    // Lightbox modal logic
    const lightbox = document.getElementById('lightbox-modal');
    if (lightbox) {
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxTitle = document.getElementById('lightbox-title');
        let currentIdx = 0;

        window.openLightbox = function (idx) {
            currentIdx = idx;
            const img = siteContent.gallery.images[currentIdx];
            if (img) {
                lightboxImg.src = resolveImageUrl(img.src);
                lightboxTitle.innerText = img.title;
                lightbox.style.display = 'flex';
            }
        };

        window.closeLightbox = function () {
            lightbox.style.display = 'none';
        };

        window.changeLightboxImage = function (n) {
            const total = siteContent.gallery.images.length;
            if (total === 0) return;
            currentIdx = (currentIdx + n + total) % total;
            const img = siteContent.gallery.images[currentIdx];
            if (img) {
                lightboxImg.src = resolveImageUrl(img.src);
                lightboxTitle.innerText = img.title;
            }
        };

        const closeBtn = lightbox.querySelector('.close');
        if (closeBtn) closeBtn.onclick = closeLightbox;

        lightbox.onclick = (e) => {
            if (e.target === lightbox || e.target.classList.contains('lightbox-container')) {
                closeLightbox();
            }
        };
    }
}

function initNewsEventsPage() {
    const pageTitle = document.getElementById('news-title');
    if (pageTitle) pageTitle.innerText = siteContent.newsEvents.title;

    const postsGrid = document.getElementById('news-posts');
    if (postsGrid) {
        postsGrid.innerHTML = siteContent.newsEvents.posts.map(post => `
            <article class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-shadow p-6 flex flex-col gap-3">
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold bg-brandCyan bg-opacity-20 text-brandCyan py-1 px-3 rounded-full uppercase tracking-wider">${post.category}</span>
                    <span class="text-xs text-slate-500 font-semibold"><i class="fa-regular fa-calendar"></i> ${post.date}</span>
                </div>
                <h4 class="text-xl font-bold text-brandNavy font-poppins hover:text-brandCyan cursor-pointer transition-colors leading-snug">${post.title}</h4>
                <p class="text-slate-600 text-sm leading-relaxed text-justify flex-grow">${post.desc}</p>
                <div class="border-t border-slate-100 pt-3 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-semibold">Posted by: arunodayapharmacy</span>
                    <a href="#" class="text-xs text-brandCyan hover:text-brandNavy font-bold uppercase tracking-wider flex items-center gap-1 group">
                        <span>Read More</span> <i class="fa-solid fa-angle-right group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </article>
        `).join('');
    }

}

function initContactPage() {
    const c = siteContent.contact;

    const pageTitle = document.getElementById('contact-title');
    if (pageTitle) pageTitle.innerText = c.title;

    const descEl = document.getElementById('contact-desc');
    if (descEl) descEl.innerText = c.description;

    // Contact Details Cards
    const officeTitle = document.getElementById('card-office-title');
    if (officeTitle) officeTitle.innerText = c.officeTitle;
    const officeAddr = document.getElementById('card-office-addr');
    if (officeAddr) officeAddr.innerText = c.officeAddress;

    const emailTitle = document.getElementById('card-email-title');
    if (emailTitle) emailTitle.innerText = c.emailTitle;
    const emailList = document.getElementById('card-email-list');
    if (emailList) {
        emailList.innerHTML = c.emailList.map(email => `<a href="mailto:${email}" class="hover:text-brandCyan block break-all font-semibold">${email}</a>`).join('');
    }

    const hoursTitle = document.getElementById('card-hours-title');
    if (hoursTitle) hoursTitle.innerText = c.hoursTitle;
    const hoursText = document.getElementById('card-hours');
    if (hoursText) hoursText.innerText = c.hours;
    const hoursSub = document.getElementById('card-hours-sub');
    if (hoursSub) hoursSub.innerText = c.subText;

    // Sidebar query
    const formTitle = document.getElementById('form-title');
    if (formTitle) formTitle.innerText = c.formTitle;
    const phoneTitle = document.getElementById('phone-title');
    if (phoneTitle) phoneTitle.innerText = c.phoneTitle;
    const phoneNum = document.getElementById('phone-num');
    if (phoneNum) phoneNum.innerText = c.phoneNumber;

    // Map box
    const mapTitle = document.getElementById('map-title');
    if (mapTitle) mapTitle.innerText = c.mapTitle;
    const mapSub = document.getElementById('map-subtitle');
    if (mapSub) mapSub.innerText = c.mapSubtitle;

    // Handle Contact Form Submit - uses FormSubmit.co to email arunodaya.pharm@gmail.com
    const form = document.getElementById('contact-form');
    const successToast = document.getElementById('success-toast');
    const errorToast = document.getElementById('error-toast');

    if (form) {
        // Configure FormSubmit hidden fields for email delivery
        const setHidden = (name, value) => {
            let inp = form.querySelector(`input[name="${name}"]`);
            if (!inp) {
                inp = document.createElement('input');
                inp.type = 'hidden';
                inp.name = name;
                form.appendChild(inp);
            }
            inp.value = value;
        };
        // FormSubmit configuration
        form.action = 'https://formsubmit.co/arunodaya.pharm@gmail.com';
        form.method = 'POST';
        setHidden('_subject', 'New Contact Form Submission - Arunodaya Institutions');
        setHidden('_captcha', 'false');
        setHidden('_template', 'table');
        setHidden('_next', window.location.href + '?submitted=true');

        // Check if returning from form submission
        if (window.location.search.includes('submitted=true')) {
            if (successToast) {
                successToast.classList.remove('hidden');
                // Remove param from URL cleanly
                const cleanUrl = window.location.pathname;
                window.history.replaceState({}, document.title, cleanUrl);
            }
        }

        form.onsubmit = function (e) {
            const name = form.querySelector('[name="name"]').value.trim();
            const email = form.querySelector('[name="email"]').value.trim();
            if (!name || !email) {
                e.preventDefault();
                if (errorToast) {
                    errorToast.classList.remove('hidden');
                    setTimeout(() => errorToast.classList.add('hidden'), 5000);
                }
                return false;
            }
            // Allow native form submit to FormSubmit.co
            return true;
        };

        // Close alert buttons
        const closeAlerts = document.querySelectorAll('.close-alert');
        closeAlerts.forEach(cBtn => {
            cBtn.onclick = function () {
                cBtn.parentElement.classList.add('hidden');
            };
        });
    }
}

// ---------------------------------
// INITIALIZATION ROUTER
// ---------------------------------

document.addEventListener("DOMContentLoaded", () => {
    // 1. Load Common layout
    renderHeader();
    renderFooter();

    // 2. Load Page Specific modules
    const path = window.location.pathname;
    const page = path.substring(path.lastIndexOf('/') + 1) || 'index.html';

    if (page === 'index.html') {
        initHomePage();
    } else if (page === 'about.html') {
        initAboutPage();
    } else if (page === 'admission-process.html') {
        initAdmissionPage();
    } else if (page === 'teaching-staff.html') {
        initTeachingStaffPage();
    } else if (page === 'non-teaching-staff.html') {
        initNonTeachingStaffPage();
    } else if (page === 'facilities.html') {
        initFacilitiesPage();
    } else if (['b-pharm.html', 'd-pharm.html', 'b-sc.html', 'b-com.html', 'bca.html'].includes(page)) {
        const courseKey = page.replace('.html', '').replace('-', '_');
        initCoursePage(courseKey);
    } else if (page === 'syllabus.html') {
        initTablePage('syllabus');
    } else if (page === 'academic-calendar.html') {
        initTablePage('academic_calendar');
    } else if (page === 'time-table.html') {
        initTablePage('time_table');
    } else if (page === 'gallery.html') {
        initGalleryPage();
    } else if (page === 'news-events.html') {
        initNewsEventsPage();
    } else if (page === 'contact-us.html') {
        initContactPage();
    }

    // 3. Initialize scroll-triggered animations
    initScrollAnimations();
});

// Scroll-triggered animations function
function initScrollAnimations() {
    const animElements = document.querySelectorAll(
        '.anim-slideInUp, .anim-slideInLeft, .anim-slideInRight, .anim-revealInLeft, .anim-fadeIn, .anim-zoomIn'
    );

    if (!('IntersectionObserver' in window)) {
        animElements.forEach(el => el.classList.add('animated'));
        return;
    }

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animElements.forEach(el => {
        observer.observe(el);
    });
}
