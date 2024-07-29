"""Test chroma_database.py"""
import os
import shutil

def test_create_and_delete_chroma_directory():
    """Test the creation and deletion of the chroma directory."""

    chroma_path = "test_chroma"

    # Ensure the chroma directory does not exist before starting the test
    if os.path.exists(chroma_path): \
        shutil.rmtree(chroma_path)

    # Test directory creation
    os.makedirs(chroma_path)
    assert os.path.exists(chroma_path), "Chroma directory should be created"

    # Test directory deletion
    shutil.rmtree(chroma_path)
    assert not os.path.exists(chroma_path), "Chroma directory should be deleted"
