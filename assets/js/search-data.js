// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/CVblog/";
    },
  },{id: "nav-이력서",
          title: "이력서",
          description: "김강민의 이력서입니다 (PDF로도 내려받을 수 있습니다).",
          section: "Navigation",
          handler: () => {
            window.location.href = "/CVblog/ko/cv/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "Curriculum vitae of Kangmin Kim — also available as a downloadable PDF.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/CVblog/cv/";
          },
        },{id: "news-launched-my-personal-academic-homepage",
          title: 'Launched my personal academic homepage. 🎉',
          description: "",
          section: "News",},{id: "news-restructured-my-homepage-added-a-full-html-cv-page-and-tidied-up-the-site-️",
          title: 'Restructured my homepage — added a full HTML CV page and tidied up...',
          description: "",
          section: "News",},{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/CVblog/assets/pdf/cv.pdf", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6D%6F%6F%6E%6C%69%67%68%74%6B%69%6D@%6B%61%69%73%74.%61%63.%6B%72", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/MoonlightWarrior", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/kangmin-kim-71401431a", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/CVblog/feed.xml", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
