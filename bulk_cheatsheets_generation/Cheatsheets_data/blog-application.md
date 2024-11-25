### Blog Application

In this assignment, let's build a Blog application by applying the concepts we have learned so far.

#### Reference

[https://s3.ap-south-1.amazonaws.com/new-assets.ccbp.in/frontend/loading-data/blog-post_hmgnss.mp4](https://s3.ap-south-1.amazonaws.com/new-assets.ccbp.in/frontend/loading-data/blog-post_hmgnss.mp4)

#### Functionalities to be Achieved:

- Display blog posts in two viewing options (grid/list), showing 6 posts per page with Previous/Next navigation buttons and current page indicator (e.g. "Page 1 of 3")


- Filter posts through categories by clicking options like All **Posts**, **Photography**, **Literature**, etc., and use search bar to find posts by title, content or tags

- Create new blog posts using "Create Post" button that opens a form to enter:

  - Title
  - Author name
  - Category selection
  - Image URL
  - Summary
  - Main content
  - Tags (comma separated)

- Show calculated reading time on each post (based on content length), formatted date, category label, and tags with hashtags (#vintage, #photography, etc.)
- Open full post details in modal window when **Read More** is clicked, displaying complete content, image and metadata

- Enable post editing through **Edit** button that:

    - Opens modal with current post data filled in
    - Updates post when changes are saved
    - Maintains same post ID and other metadata
    - Post should appear in same place after update
    - Form fields retain existing post data


- Allow post deletion with confirmation message before removing from list

    - Updates pagination after deletion
    - Maintains current page if possible


- Display **Popular Posts** section in sidebar showing top 3 posts based on number of likes
- Track post count for pagination:

    - Update total pages when posts are added/deleted
    - Keep user on current page when possible
    - Reset to page 1 if current page no longer exists


- Show error messages when required fields are missing during create/edit (title, author, content, etc.)

- When **Publish Post** or **Update Post** is clicked:

    - Validate all required fields
    - Add/Update post immediately
    - Update pagination accordingly
    - Close modal after success
    - Show post in correct position

- Post Object Format (For Reference)

```
const postFormat = {
    id: 1,                    // Unique post identifier
    title: "Sample Title",    // Post title
    author: "Author Name",    // Author name
    date: "2024-03-15",      // Post date
    category: "photography",  // Post category
    summary: "Brief text...", // Short description
    content: "Full text...",  // Main post content
    imageUrl: "url/here",     // Image link
    tags: ["tag1", "tag2"],   // Post tags array
    likes: 245,              // Number of likes
    readTime: "5 min",       // Reading duration
    featured: true           // Featured status
}
```

#### Submission Instructions

- Publish your project as a code snippet in learning portal or any other deployment platform
- Submit your project in this [form]()

### Highlight Your Technical Excellence!

<MultiLineNote>
<div style="display: flex; flex-wrap: wrap; gap: 40px; padding: 30px; background: linear-gradient(to right, #f0f2f5, #ffffff); border-radius: 12px; max-width: 1200px; margin: 20px auto;">
    <div style="flex: 1 1 300px;">
        <h2 style="font-family: Arial, sans-serif; color: #0a66c2; margin: 0 0 15px 0; font-size: clamp(1.5rem, 4vw, 2.5rem);">Share on LinkedIn</h2>
        <p style="color: #666; line-height: 1.5;">Let your work speak for itself. Showcase your achievements and connect with professionals who share your passion.</p>
        <a href="https://www.linkedin.com" 
           style="display: inline-block; margin-top: 15px; padding: 10px 20px; background-color: #0a66c2; color: white; text-decoration: none; border-radius: 5px; font-family: Arial, sans-serif;">
            LinkedIn.com
        </a>
    </div>
    <div style="flex: 0 1 300px;">
        <img src="https://res.cloudinary.com/dpvbaiyus/image/upload/v1730870613/programmer-work-laptop-computer-website-code-program-concept_133260-5402_ffsbmo.avif" 
             style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" 
             alt="Programmer working on laptop">
    </div>
</div>
</MultiLineNote>
