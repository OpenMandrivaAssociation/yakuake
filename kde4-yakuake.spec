%define origname yakuake

Summary:	Very powerful Quake style Konsole
Name:		kde4-%origname
Version:	2.9.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source:		http://download.berlios.de/%{name}/%{origname}-%{version}.tar.bz2
Url:		http://www.kde-apps.org/content/show.php?content=29153
BuildRequires:	kdelibs4-devel
Requires:       kde4-konsole
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Yakuake is a Quake-style terminal emulator based on KDE Konsole technology.

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{origname}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README TODO NEWS KDE4FAQ
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/%{origname}
%{_kde_iconsdir}/hicolor/*/apps/*


#--------------------------------------------------------------------

%prep 
%setup -qn %{origname}-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd -

%find_lang %origname

%clean 
rm -rf %{buildroot} 
