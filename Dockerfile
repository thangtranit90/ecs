FROM nginx

COPY index.html /usr/share/nginx/html/index.html
COPY customngix.conf /etc/nginx/nginx.conf


EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
