# **iTrackFiles**

*iTrackFiles* is a Django-based web application designed for efficient document and image management. This application simplifies the process of uploading, organizing, and retrieving scanned and imported files, providing seamless integration with scanners and file directories.

## **Features**
- **Batch Management**: Create, update, and organize document batches for streamlined operations.
- **Image Processing**:
  - Upload and scan images.
  - View and manage images, including deletion and reordering.
- **Search Functionality**: Search documents by categories like Adoption, Criminal, Civil, Historic Index Cards, and more.
- **Dynamic Template System**: Tailored templates for various document types and use cases.
- **User Session Management**: Limit user sessions to ensure security and enable seamless re-login.
- **Admin Controls**:
  - Manage users without handling their passwords directly.
  - Reset passwords securely, allowing users to change them later.

## **Technologies Used**
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript (UI components built with UIKit)
- **Database**: SQLite (can be replaced with other RDBMS for production)
- **File Management**: Static and media file handling with Django's STATICFILES_DIRS and MEDIA_ROOT
