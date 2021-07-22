const collapseNavbarBtn = document.getElementById("collapse_navbar");

const collapse_navbar_callback = () => {
	collapseNavbarBtn.onclick = () => {
		const sideNavbar = document.getElementsByClassName("sidenavbar_container")[0];
		const collapsables = document.getElementsByClassName('collapsable');
		const nonCollapse = document.getElementsByClassName('non-collapse');
		const brandCollapse = document.getElementsByClassName('brand-collapse')[0];
		sideNavbar.classList.toggle('col-3');
		sideNavbar.classList.toggle('col-1');
		
		if (brandCollapse.textContent === 'TweakTime') {
			brandCollapse.textContent = 'TT';
			console.log('here1')
		} else {
			console.log('here2')
			brandCollapse.textContent = 'TweakTime';
		}

		for (let i = 0; i < collapsables.length; i++) {
			collapsables[i].classList.toggle('collapsed');
		}

		for (let i = 0; i < collapsables.length; i++) {
			nonCollapse[i].classList.toggle('fs-1');
		}
	};
}


collapse_navbar_callback();
