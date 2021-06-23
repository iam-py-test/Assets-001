/// cookie-set.js
/// alias cs.js
// example.com##+js(cs, name, value, age)
(() => {
		'use strict';
		const cs = ev => {
					if (ev) { window.removeEventListener(ev.type, cs, true); }
					try {
						document.cookie = '{{1}}={{2}}; max-age={{3}}; secure; path=/;';
					} catch { }
	   	};
	   	if (document.readyState === 'loading') {
		    	 window.addEventListener('DOMContentLoaded', cs, true);
	   	} else {
		    	 cs();
	   	}
})();	
